# YouTube Downloader

## Introduction
This command-line tool allows you to download YouTube videos, playlists, songs from a file, or search and download directly. It is developed using Python and the `pytubefix` library.

## Installation
1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the required dependencies using pip:

pip install -r requirements.txt


## Usage
Navigate to the directory where the tool is located and run the `main.py` script using Python.

### Command Line Arguments
- `-v, --video`: Downloads a single video from the provided YouTube URL.
- `-p, --playlist`: Downloads all videos in the provided YouTube playlist URL.
- `-f, --file`: Reads a text file containing song names (separated by newlines) and downloads them.
- `-d, --download`: Searches for a song on YouTube and downloads it.
- `-r, --raw`: (Optional) Download videos in MP4 format instead of MP3.

### Examples

#1. Download a video:

python main.py -v https://www.youtube.com/watch?v=VIDEO_ID


# 2. Download a playlist:

python main.py -p https://www.youtube.com/playlist?list=PLAYLIST_ID


# 3. Download songs from a file:

python main.py -f songs.txt


# 4. Search and download a song:

python main.py -d "Song Name"


# 5. Download videos in MP4 format:

python main.py -v https://www.youtube.com/watch?v=VIDEO_ID -r


### Additional Notes
- Make sure you installed FFMPEG and added the /bin folder to your path
- Make sure you have a stable internet connection.
- The tool will automatically convert videos to MP3 format unless the `-r` flag is used.
- Ensure that the provided URLs are valid YouTube URLs.

## Author
Vivian

