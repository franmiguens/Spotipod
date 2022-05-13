import SpotifyComm
import YouTubeComm
import Tagging
import EditTextFiles
from os.path import exists
text_file_path = '/Users/franciscomiguens/Desktop/Coding/text files'
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Features to add
#1) Check which songs are already downloaded from each playlist, dont download again.
#2) Select which playlists to download
#3) Path input and os detection
#4) Add a clean up function, suggests removing songs and removes extra files


def main():
    print('Getting playlist...')
    all_playlists = SpotifyComm.get_playlists()
    print('Done')
    for playlist_name in all_playlists:
        safe_string = playlist_name[0]
        if '/' in safe_string:
            safe_string = safe_string.replace('/', '~')
        if exists(text_file_path+'/'+safe_string) == False:
            open(text_file_path+'/'+safe_string, 'x')
    for x in all_playlists:
        print('Getting '+x[0]+' tracks...')
        playlist = SpotifyComm.get_tracks_in_playlist(x[2])
        safe_string = x[0]
        if '/' in safe_string:
            safe_string = safe_string.replace('/', '~')
        playlist = EditTextFiles.edit_text_files(playlist, text_file_path+'/'+safe_string)
        print('Done')
        print('Searching YouTube, Downloading M4A...')
        for y in playlist:
            video_id = YouTubeComm.get_videos(y[0]+' '+y[1])
            directory = YouTubeComm.download_audio('https://www.youtube.com/watch?v='+video_id, x[0])

            Tagging.metadata(directory, SpotifyComm.get_metadata(y[2]))
        print('Done')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
