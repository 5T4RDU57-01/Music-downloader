# YouTube Downloader Tool

This command-line tool written in Python allows users to download YouTube videos and playlists. It supports downloading videos from URLs, playlists, video names listed in a file, and searching and downloading videos by name.

## Usage

### Prerequisites

- Python 3.x
- `pytube` library (`pip install pytube`)
- `youtubesearchpython` library (`pip install youtubesearchpython`)

### Command Line Arguments

- `-v`, `--video <url>`: Download a YouTube video by URL.
- `-p`, `--playlist <url>`: Download a YouTube playlist by URL.
- `-f`, `--file <filename>`: Read video names from a file and download them.
- `-d`, `--download <songname>`: Search for a video by name and download it.

### Example Usage

# Download a video:

python main.py -v https://www.youtube.com/watch?v=VIDEO_ID


# Download a playlist:

python main.py -p https://www.youtube.com/playlist?list=PLAYLIST_ID


# Download videos from a file:

python main.py -f videos.txt


# Search and download a video:

python main.py -d "Song Name"


## Files

- `main.py`: Contains the main program logic and command-line argument parsing.
- `helpers.py`: Contains functions for downloading videos, playlists, and searching for videos by name.

## How It Works

- The `main.py` file handles command-line arguments using the `argparse` library.
- Video downloading functionality is implemented in the `helpers.py` file using the `pytube` library for downloading videos and playlists and the `youtubesearchpython` library for searching videos by name.

## Usage Notes

- Make sure to provide valid YouTube URLs for videos and playlists.
- Video names should be listed one per line in the input file for the `-f` option.
- Use double quotes (`"`) around song names when using the `-d` option to search by name.

## Running the Program

1. Install Python 3.x, `pytube`, and `youtubesearchpython` libraries.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `main.py` and `helpers.py`.
4. Use the command-line arguments as described above to download YouTube videos and playlists.

