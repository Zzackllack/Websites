import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
from tqdm import tqdm
import urllib.request
import re
import tkinter as tk
from tkinter import messagebox, filedialog

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize_filename(filename):
    # Entferne ungültige Zeichen aus dem Dateinamen
    return re.sub(r'[^a-zA-Z0-9_\-.]', '_', filename)[:255]

def is_valid_url(url):
    # Überprüft, ob die URL ein gültiges HTTP(S)-Schema hat
    parsed = urlparse(url)
    return bool(parsed.scheme in ('http', 'https') and parsed.netloc)

def is_valid_directory(directory):
    # Überprüft, ob der Pfad gültig ist
    return os.path.isdir(directory) or not os.path.exists(directory)

def download_file(url, directory, logger, progress_bar):
    local_filename = sanitize_filename(url.split('/')[-1])
    full_path = os.path.join(directory, local_filename)
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(full_path, 'wb') as file, tqdm(
        desc=local_filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
        leave=False,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
            progress_bar.update(size)
    
    logger.info(f"Downloaded {url} to {full_path}")
    return full_path

def extract_media_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    media_files = {
        'images': [],
        'videos': [],
        'audios': [],
        'documents': [],
        'external_links': []
    }
    video_host_domains = ["voe.sx", "doodstream.com", "vidoza.net", "streamtape.com"]
    document_extensions = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt']

    # Extract images
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            if is_valid_url(img_url):
                media_files['images'].append(img_url)

    # Extract videos
    for video_tag in soup.find_all('video'):
        video_url = video_tag.get('src')
        if video_url:
            video_url = urljoin(url, video_url)
            if is_valid_url(video_url):
                media_files['videos'].append(video_url)
        # Also check for source tags within video tag
        for source_tag in video_tag.find_all('source'):
            video_url = source_tag.get('src')
            if video_url:
                video_url = urljoin(url, video_url)
                if is_valid_url(video_url):
                    media_files['videos'].append(video_url)

    # Extract audios
    for audio_tag in soup.find_all('audio'):
        audio_url = audio_tag.get('src')
        if audio_url:
            audio_url = urljoin(url, audio_url)
            if is_valid_url(audio_url):
                media_files['audios'].append(audio_url)
        # Also check for source tags within audio tag
        for source_tag in audio_tag.find_all('source'):
            audio_url = source_tag.get('src')
            if audio_url:
                audio_url = urljoin(url, audio_url)
                if is_valid_url(audio_url):
                    media_files['audios'].append(audio_url)

    # Extract documents
    for a_tag in soup.find_all('a', href=True):
        link_url = a_tag['href']
        if link_url.startswith('javascript:'):
            continue
        full_link_url = urljoin(url, link_url)
        file_extension = full_link_url.split('.')[-1].lower()
        if file_extension in document_extensions and is_valid_url(full_link_url):
            media_files['documents'].append(full_link_url)
        elif any(domain in full_link_url for domain in video_host_domains):
            media_files['external_links'].append(full_link_url)
        else:
            media_files['external_links'].append(full_link_url)

    # Extract hidden video links for Streamtape
    for hidden_link_id in ['ideoolink', 'robotlink', 'botlink']:
        hidden_link_tag = soup.find(id=hidden_link_id)
        if hidden_link_tag and hidden_link_tag.text:
            hidden_link_url = hidden_link_tag.text.strip()
            if hidden_link_url.startswith('//'):
                hidden_link_url = 'https:' + hidden_link_url
            if is_valid_url(hidden_link_url):
                media_files['videos'].append(hidden_link_url)

    return media_files

def collect_stats(media_files):
    stats = {
        'images': len(media_files['images']),
        'videos': len(media_files['videos']),
        'audios': len(media_files['audios']),
        'documents': len(media_files['documents']),
        'external_links': len(media_files['external_links'])
    }
    return stats

def download_media(media_files, base_directory, media_types, logger):
    if "all" in media_types:
        media_types = list(media_files.keys())  # Download all media types

    # Calculate total size of all downloads for the progress bar
    total_size = 0
    for media_type in media_types:
        if media_type in media_files:
            for url in media_files[media_type]:
                if is_valid_url(url):
                    response = requests.head(url)
                    total_size += int(response.headers.get('content-length', 0))

    with tqdm(total=total_size, unit='iB', unit_scale=True, unit_divisor=1024, desc="Total Progress") as progress_bar:
        for media_type in media_types:
            if media_type in media_files:
                media_directory = os.path.join(base_directory, media_type)
                create_directory(media_directory)
                if media_type == 'external_links':
                    # Save external links to links.txt
                    links_file = os.path.join(media_directory, 'links.txt')
                    with open(links_file, 'w') as file:
                        for url in media_files[media_type]:
                            file.write(url + '\n')
                    logger.info(f"External links saved to {links_file}")
                else:
                    for url in media_files[media_type]:
                        if is_valid_url(url):
                            logger.info(f"Downloading {url}")
                            download_file(url, media_directory, logger, progress_bar)

def on_browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)

def on_start():
    url = entry_url.get()
    base_directory = entry_directory.get()
    media_types = entry_media_types.get().split(',')

    media_types = [media_type.strip() for media_type in media_types]
    valid_media_types = {'images', 'videos', 'audios', 'documents', 'external_links', 'all'}

    if not is_valid_url(url):
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with http:// or https://")
        return

    if not is_valid_directory(base_directory):
        messagebox.showerror("Invalid Directory", "Please enter a valid directory path.")
        return

    if not all(media_type in valid_media_types for media_type in media_types):
        messagebox.showerror("Invalid Media Types", f"Please enter valid media types: {', '.join(valid_media_types)}")
        return

    create_directory(base_directory)

    print("Please wait, the script might be unresponsive while processing...")

    # Configure logging
    sanitized_url = sanitize_filename(url.replace('https://', '').replace('http://', '').replace('/', '_'))
    log_filename = os.path.join(base_directory, f"log-{sanitized_url}.txt")
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()

    media_files = extract_media_from_url(url)
    stats = collect_stats(media_files)
    
    logger.info("Statistics of the webpage:")
    for key, value in stats.items():
        logger.info(f"{key.capitalize()}: {value}")

    download_media(media_files, base_directory, media_types, logger)
    
    logger.info("Processing complete. Media files have been processed.")
    
    messagebox.showinfo("Complete", f"Processing complete. Log file saved as {log_filename}.")

# Create the main window
root = tk.Tk()
root.title("Media Downloader")

# Configure the grid
root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# Create and place the URL entry field
tk.Label(root, text="Enter the URL of the webpage to scan:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Create and place the directory entry field
tk.Label(root, text="Enter the directory to save the downloaded media:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_directory = tk.Entry(root)
entry_directory.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
tk.Button(root, text="Browse...", command=on_browse_directory).grid(row=1, column=2, padx=10, pady=5, sticky="w")

# Create and place the media types entry field
tk.Label(root, text="Enter the types of media to download (comma-separated):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_media_types = tk.Entry(root)
entry_media_types.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Create and place the start button
tk.Button(root, text="Start", command=on_start).grid(row=3, column=1, padx=10, pady=20, sticky="e")

# Run the main event loop
root.mainloop()
