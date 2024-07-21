# Website-scanner

Website-scanner is a Python tool designed to scan a webpage for various types of media files, including images, videos, audios, and links to external video hosting sites. The tool downloads the found media files to a specified directory and logs the results for easy reference.

## Features

- Scans a webpage for images, videos, audios, and external links
- Downloads found media files to a specified directory
- Logs all actions and found links in a log file
- Displays download progress with a progress bar for large files
- User-friendly input validation for media types

## Requirements

- Python 3.6+
- The following Python libraries:
  - requests
  - BeautifulSoup4
  - tqdm
  - urllib

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/website-scanner.git
   cd website-scanner
   ```

2. **(Optional) Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Website-scanner, run the script and follow the prompts:

```bash
python website_scanner.py
```

### Example

1. **Enter the URL of the webpage to scan:**

   ```
   Enter the URL of the webpage to scan: https://example.com
   ```

2. **Enter the directory to save the downloaded media:**

   ```
   Enter the directory to save the downloaded media: ./downloaded_media
   ```

3. **Enter the types of media to download:**

   ```
   Enter the types of media to download (options: images, videos, audios, external_links, all, comma-separated): images, videos
   ```

The script will then process the URL, download the specified media files, and save the log file in the specified directory.

## Logging

The script creates a log file in the specified download directory. The log file contains:

- Information about the downloaded files
- External links found on the webpage
- Any errors encountered during the process

## License

This project is licensed under the same License as the "Websites" repository.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me.
