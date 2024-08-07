from pytubefix import YouTube, Playlist, Search
from pytubefix.cli import on_progress
from re import match
from os.path import basename, splitext, exists
from os import remove
from subprocess import call


class Downloader:
    def __init__(self, change_ext=True) -> None:
        self.change_ext = change_ext

    # Download a video with the given URL
    # Is also used in the download playlist function, the video object can be given as an arg
    def download_video(self, url: str = None, youtube_object=None) -> int:

        try:
            if url is not None:
                video = YouTube(url)

            if youtube_object is not None:
                video = youtube_object

            print(f"\nDownloading {video.title}")

            if self.change_ext:
                stream = video.streams.get_audio_only()
            else:
                try:
                    stream = video.streams.get_by_resolution()
                except:
                    pass

            if stream is None:
                print(f"Could not download {video.title} in Mp4, downloading in mp3")
                stream = video.streams.get_audio_only()

            stream.download(mp3=self.change_ext)

            # if self.change_ext:
            #     self.change_extention_to_mp3(downloaded_file)

        except KeyError:
            return 1

        print("Download successful!\n")



        return 0

    # Download all the videos in a playlist with the given URL
    def download_playlist(self, url: str) -> int:

        try:
            pl = Playlist(url)
        except:
            return 1

        for vid in pl.videos:
            self.download_video(youtube_object=vid)

        return 0

    # Read a text file with the songnames (seperated by newlines)
    # and download all of them
    def download_from_file(self, file: str) -> int:
        songs = None

        with open(file, "r") as songfile:
            songs = songfile.readlines()

        for song in songs:
            self.search_and_download(song=song)

        return 0

    # Search a song on youtube an download it
    def search_and_download(self, song: str) -> int:

        result = (Search(f"{song} song").results)[0]

        self.download_video(youtube_object=result)
        return 0

    # Chnage the extention of a file to MP3
    @staticmethod
    def change_extention_to_mp3(file: str) -> None:


        file = basename(file)
        base, ext = splitext(file)

        command = "ffmpeg -i {} -vn -ar 44100 -ac 2 -b:a 192k {}".format(f'"{file}"', f'"{base}.mp3"')
        call(command, shell=True)

        remove(file)

        


# Validate a youtube URL (can be playlist or video)
def validate_url(url: str) -> bool:
    matched = match(
        r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$",
        url,
    )

    return matched != None


# See if a file exists and is a text file
def validate_file(filename: str) -> bool:
    return exists(filename) and basename(filename).endswith(".txt")
