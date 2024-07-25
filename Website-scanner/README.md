# Website-scanner

Website-scanner is a Python tool designed to scan a webpage for various types of media files, including images, videos, audios, documents, and links to external video hosting sites. The tool downloads the found media files to a specified directory and logs the results for easy reference. Additionally, it provides a user-friendly GUI for easier interaction.

## Features

- **NEW**: Scans a webpage for images, videos, audios, documents, and external links
- Downloads found media files to a specified directory
- Logs all actions and found links in a log file
- Displays download progress with a progress bar for large files
- **HUGE UPDATE**: Collects and logs statistics about the scanned webpage
- User-friendly input validation for media types and directory paths
- **MODERN UPDATE**: Graphical User Interface (GUI) for easier interaction

# Easy Way to Use

The easiest way to use the Website-scanner on Windows is to run the provided `.exe` file. This allows you to use the program without needing to install Python or any additional dependencies.

## Steps

1. **Download the `downloader.exe` file** from the repository.

2. **Run the `downloader.exe`**:
   - Simply double-click the `downloader.exe` file.
   - The application window will open with the title "Website-scanner by Zzackllack".

3. **Using the Application**:
   - Enter the URL of the webpage you want to scan.
   - Choose the directory where you want to save the downloaded media files.
   - Specify the types of media you want to download (images, videos, audios, documents, external_links, or all).
   - Click the "Start" button to begin the scanning and downloading process.

## Features of the `.exe` Version

- **No Python Installation Required**: Run the program directly on Windows without installing Python or other libraries.
- **User-Friendly GUI**: A graphical interface that makes it easy to input URLs, select directories, and choose media types.
- **Custom Icon and Title**: The application runs with a custom icon and the title "Website-scanner by Zzackllack".
- **Multilingual Support**: The program supports both English and German based on your system's language settings.

This method is recommended for users who prefer a straightforward and hassle-free setup.
****

## Requirements for Python Version

- Python 3.6+
- The following Python libraries:
  - requests
  - BeautifulSoup4
  - tqdm
  - urllib
  - tkinter

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

To use the Website-scanner with the GUI, run the script:

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
   Enter the types of media to download (options: images, videos, audios, documents, external_links, all, comma-separated): images, videos
   ```

The script will then process the URL, download the specified media files, and save the log file in the specified directory.

## GUI Usage

**NEW INNOVATIVE UPDATE:**

1. **URL Field:**
   Enter the URL of the webpage you want to scan.

2. **Directory Field:**
   Enter the directory where you want the downloaded media to be saved, or use the "Browse..." button to select a directory.

3. **Media Types Field:**
   Enter the types of media you want to download (e.g., images, videos, audios, documents, external_links, all).

4. **Start Button:**
   Click "Start" to begin the scanning and downloading process.

## Logging

The script creates a log file in the specified download directory. The log file contains:

- Information about the downloaded files
- External links found on the webpage
- Any errors encountered during the process
- **UPDATED VERSION**: Statistics about the scanned webpage, such as the number of each type of media found

## License

This project is licensed under the same License as the "Websites" repository.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me.
