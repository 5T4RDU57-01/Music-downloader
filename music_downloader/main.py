from argparse import ArgumentParser, Namespace
from helpers import Downloader, validate_url, validate_file


def main():
    args: Namespace = get_args()

    code: int = do_everything(args=args)

    give_message(code)

    return 0

# Downloads the video, playlist, videos from a file or from a searh
def do_everything(args: Namespace) -> int:

    change_ext = not args.raw

    down = Downloader(change_ext=change_ext)
    # <VIDEO>
    if args.video:
        if validate_url(args.video[0]):
            down.download_video(args.video[0])
        else:
            return 1
    # <!VIDEO>
        
    # <PLAYLIST>
    if args.playlist:
        if validate_url(args.playlist[0]):
            down.download_playlist(args.playlist[0])
        else:
            return 1
    # <!PLAYLIST>
        
    # <FILE>
    if args.file:
        if validate_file(args.file[0]):
            down.download_from_file(args.file[0])
        else:
            return 2
    # <!FILE>
        
    # <SEARCH>
    if args.download:
        down.search_and_download(args.download[0])
    # <!SEARCH>

    return 0 


# Return the namespace with all the given arguments
def get_args() -> Namespace:
    parser = ArgumentParser()


    group = parser.add_mutually_exclusive_group(required=True)

    # <!VIDEO>
    group.add_argument("-v", "--video", 
                       help="Given a YouTube URL, download the video", 
                       metavar=("url"), 
                       nargs=1)
    # <!VIDEO>
    
    # <PLAYLIST>
    group.add_argument("-p", "--playlist",
                       help="Given a YouTube URL, download the playlist", 
                       metavar=("url"), 
                       nargs=1)
    # <!PLAYLIST>
    
    # <FILE>

    group.add_argument("-f", "--file", 
                       help="Given a text file, download all the songs in it (seperated by newlines)", 
                       metavar="filename", 
                       nargs=1)
    # <!FILE>

    # <SEARCH>
    group.add_argument("-d", "--download", 
                       help="Given the name of a song, download it", 
                       metavar=("songname"), 
                       nargs=1)
    # <!SEARCH>

    # <DOWNLOAD AS MP4>
    parser.add_argument("-r", "--raw",
                        help="Download the video as MP4",
                        action="store_true",
                        default=False
                        )
    # <DOWNLOAD AS MP4>
    



    args: Namespace = parser.parse_args()

    return args


# Print a message given a code
def give_message(code: int) -> None:
    messages: dict = {
        0 : "Action completed successfully!",
        1 : "Incorrect URL, please fix thanxx <3",
        2 : "File does not exist or is not a text file :3",
    }

    print(messages[code])


if __name__ == "__main__":
    main()