import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
from tqdm import tqdm
import urllib.request
import re
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import threading
import locale

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
    
    with open(full_path, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.step(size)
    
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

def download_media(media_files, base_directory, media_types, logger, progress_bar):
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

    progress_bar["maximum"] = total_size

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
        messagebox.showerror(messages['invalid_url_title'], messages['invalid_url_message'])
        return

    if not is_valid_directory(base_directory):
        messagebox.showerror(messages['invalid_directory_title'], messages['invalid_directory_message'])
        return

    if not all(media_type in valid_media_types for media_type in media_types):
        messagebox.showerror(messages['invalid_media_types_title'], messages['invalid_media_types_message'])
        return

    create_directory(base_directory)

    progress_bar.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    processing_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Start the processing in a new thread
    threading.Thread(target=process, args=(url, base_directory, media_types)).start()

def process(url, base_directory, media_types):
    # Configure logging
    sanitized_url = sanitize_filename(url.replace('https://', '').replace('http://', '').replace('/', '_'))
    log_filename = os.path.join(base_directory, f"log-{sanitized_url}.txt")
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()

    media_files = extract_media_from_url(url)
    stats = collect_stats(media_files)
    
    logger.info(messages['stats_message'])
    for key, value in stats.items():
        logger.info(f"{key.capitalize()}: {value}")

    download_media(media_files, base_directory, media_types, logger, progress_bar)
    
    logger.info(messages['processing_complete_message'])
    
    messagebox.showinfo(messages['complete_title'], f"{messages['complete_message']} {log_filename}.")

# Detect system language
lang, _ = locale.getdefaultlocale()

# Define messages based on language
if lang.startswith("de"):
    messages = {
        "invalid_url_title": "Ungültige URL",
        "invalid_url_message": "Bitte geben Sie eine gültige URL ein, die mit http:// oder https:// beginnt.",
        "invalid_directory_title": "Ungültiges Verzeichnis",
        "invalid_directory_message": "Bitte geben Sie einen gültigen Verzeichnispfad ein.",
        "invalid_media_types_title": "Ungültige Medientypen",
        "invalid_media_types_message": "Bitte geben Sie gültige Medientypen ein: images, videos, audios, documents, external_links, all",
        "processing_message": "Bei Webseiten mit vielen/großen Mediendateien kann es sein, dass das Programm möglicherweise nicht reagiert, haben Sie bitte Geduld.",
        "stats_message": "Statistiken der Webseite:",
        "processing_complete_message": "Verarbeitung abgeschlossen. Mediendateien wurden verarbeitet.",
        "complete_title": "Fertig",
        "complete_message": "Verarbeitung abgeschlossen. Protokolldatei gespeichert als"
    }
else:
    messages = {
        "invalid_url_title": "Invalid URL",
        "invalid_url_message": "Please enter a valid URL starting with http:// or https://",
        "invalid_directory_title": "Invalid Directory",
        "invalid_directory_message": "Please enter a valid directory path.",
        "invalid_media_types_title": "Invalid Media Types",
        "invalid_media_types_message": "Please enter valid media types: images, videos, audios, documents, external_links, all",
        "processing_message": "For websites with many/large media files, the program may become unresponsive. Please be patient.",
        "stats_message": "Statistics of the webpage:",
        "processing_complete_message": "Processing complete. Media files have been processed.",
        "complete_title": "Complete",
        "complete_message": "Processing complete. Log file saved as"
    }

# Create the main window
root = tk.Tk()
root.title("Media Downloader")

# Configure the grid
root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)

# Create and place the URL entry field
tk.Label(root, text=messages["invalid_url_message"]).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Create and place the directory entry field
tk.Label(root, text=messages["invalid_directory_message"]).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_directory = tk.Entry(root)
entry_directory.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
tk.Button(root, text="Browse...", command=on_browse_directory).grid(row=1, column=2, padx=10, pady=5, sticky="w")

# Create and place the media types entry field
tk.Label(root, text=messages["invalid_media_types_message"]).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_media_types = tk.Entry(root)
entry_media_types.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Create and place the start button
tk.Button(root, text="Start", command=on_start).grid(row=3, column=1, padx=10, pady=20, sticky="e")

# Create and place the progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")

# Create and place the processing message label
processing_label = tk.Label(root, text=messages["processing_message"])

# Run the main event loop
root.mainloop()
