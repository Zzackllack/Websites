import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
from tqdm import tqdm
import urllib.request

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_file(url, directory, logger):
    local_filename = url.split('/')[-1]
    full_path = os.path.join(directory, local_filename)
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(full_path, 'wb') as file, tqdm(
        desc=local_filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
    
    logger.info(f"Downloaded {url} to {full_path}")
    return full_path

def extract_media_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    media_files = {'images': [], 'videos': [], 'audios': [], 'external_links': []}
    video_host_domains = ["voe.sx", "doodstream.com", "vidoza.net", "streamtape.com"]

    # Extract images
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            media_files['images'].append(img_url)

    # Extract videos
    for video_tag in soup.find_all('video'):
        video_url = video_tag.get('src')
        if video_url:
            video_url = urljoin(url, video_url)
            media_files['videos'].append(video_url)
        # Also check for source tags within video tag
        for source_tag in video_tag.find_all('source'):
            video_url = source_tag.get('src')
            if video_url:
                video_url = urljoin(url, video_url)
                media_files['videos'].append(video_url)

    # Extract audios
    for audio_tag in soup.find_all('audio'):
        audio_url = audio_tag.get('src')
        if audio_url:
            audio_url = urljoin(url, audio_url)
            media_files['audios'].append(audio_url)
        # Also check for source tags within audio tag
        for source_tag in audio_tag.find_all('source'):
            audio_url = source_tag.get('src')
            if audio_url:
                audio_url = urljoin(url, audio_url)
                media_files['audios'].append(audio_url)

    # Extract external links
    for a_tag in soup.find_all('a', href=True):
        link_url = a_tag['href']
        if link_url.startswith('javascript:'):
            continue
        full_link_url = urljoin(url, link_url)
        if any(domain in full_link_url for domain in video_host_domains):
            media_files['external_links'].append(full_link_url)
        else:
            media_files['external_links'].append(full_link_url)

    return media_files

def download_media(media_files, base_directory, media_types, logger):
    if "all" in media_types:
        media_types = list(media_files.keys())  # Download all media types

    for media_type in media_types:
        if media_type in media_files:
            media_directory = os.path.join(base_directory, media_type)
            create_directory(media_directory)
            for url in media_files[media_type]:
                if media_type != 'external_links':  # Only download if it's not an external link
                    logger.info(f"Downloading {url}")
                    download_file(url, media_directory, logger)
                else:
                    logger.info(f"Found external link: {url}")

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to scan: ")
    base_directory = input("Enter the directory to save the downloaded media: ")

    valid_media_types = {'images', 'videos', 'audios', 'external_links', 'all'}
    
    while True:
        media_types = input("Enter the types of media to download (options: images, videos, audios, external_links, all, comma-separated): ").split(',')
        media_types = [media_type.strip() for media_type in media_types]
        
        if all(media_type in valid_media_types for media_type in media_types):
            break
        else:
            print(f"Invalid media types entered. Please enter valid options: {', '.join(valid_media_types)}")

    create_directory(base_directory)

    # Configure logging
    log_filename = os.path.join(base_directory, f"log-{url.replace('https://', '').replace('http://', '').replace('/', '_')}.txt")
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()

    media_files = extract_media_from_url(url)
    download_media(media_files, base_directory, media_types, logger)
    
    logger.info("Processing complete. Media files have been processed.")
    logger.info("External links found:")
    for link in media_files['external_links']:
        logger.info(link)
    
    print(f"Processing complete. Log file saved as {log_filename}.")
