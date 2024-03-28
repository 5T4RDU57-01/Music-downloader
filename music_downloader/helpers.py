from youtubesearchpython import VideosSearch
from pytube import YouTube, Playlist
from re import match
from os.path import basename, splitext, exists
from os import rename

# Download a video with the given URL
# Is also used in the download playlist function, the video object can be given as an arg
def download_video(url:str=None, playlist_vid=None) -> int:
    try:
        
        if url is not None:
            video = YouTube(url)
        
        elif playlist_vid is not None:
            video = playlist_vid
            
        print(f'\nDownloading {video.title}')
        stream = video.streams.filter(only_audio=True).first()
        
        downloaded_file = stream.download()
        change_extention_to_mp3(downloaded_file)
        print('Download successful!\n')
        
    except KeyError:
        return 1
    
    return 0


# Download all the videos in a playlist with the given URL
def download_playlist(url:str) -> int:

    try:
        pl = Playlist(url)
    except:
        return 1
    
    for vid in pl.videos:
        download_video(playlist_vid=vid)
        
    return 0
                 

# Read a text file with the songnames (seperated by newlines)
# and download all of them
def download_from_file(file: str) -> int:
    songs = None

    with open(file, 'r') as songfile:
        songs = songfile.readlines()

    for song in songs:
        search_and_download(song=song)

    return 0


# Search a song on youtube an download it
def search_and_download(song: str) -> int:
    
    result = VideosSearch(song + 'song' , limit=1).result()

    id = (result['result'])[0]['id']
    url = f'https://www.youtube.com/watch?v={id}'
    download_video(url=url)
    return 0


# Chnage the extention of a file to MP3
def change_extention_to_mp3(file: str) -> None:

    file = basename(file)

    base, ext = splitext(file)
    new_file = base + '.mp3'
    rename(file, new_file)


# Validate a youtube URL (can be playlist or video)
def validate_url(url: str) -> bool:
    matched = match(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', url)

    return (matched != None)


# See if a file exists and is a text file
def validate_file(filename:str) -> bool:
    return (exists(filename) and 
            basename(filename).endswith(".txt"))