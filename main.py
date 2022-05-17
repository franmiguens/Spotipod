import SpotifyComm
import YouTubeComm
import Tagging
import EditTextFiles
import SpecificPlaylistSelection
from os.path import exists
text_file_path = '/Users/franciscomiguens/Desktop/Coding/text files'
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Features to add
#1) Select which playlists to download
#2) Path input and os detection
#3) Add a clean up function, suggests removing songs and removes extra files. Cleans up after aborted sequence
#4)Add genre Metadata


def main():
    print('Getting playlist...')
    all_playlists = SpotifyComm.get_playlists()
    all_playlists = SpecificPlaylistSelection.select(all_playlists)
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
            bad_download = True
            while bad_download:
                bad_download = YouTubeComm.download_audio('https://www.youtube.com/watch?v='+video_id, x[0], y[0])
            directory = '/Users/franciscomiguens/Desktop/Coding/music/'+x[0]+'/'+y[0]+'.m4a'
            Tagging.metadata(directory, SpotifyComm.get_metadata(y[2]))
        print('Done')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
