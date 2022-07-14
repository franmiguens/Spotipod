import SpotifyComm
import YouTubeComm
import Tagging
import EditTextFiles
import SpecificPlaylistSelection
from os.path import exists

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Features to add
#1) Select which playlists to download
#2) Path input and os detection
#3) Add a clean up function, suggests removing songs and removes extra files. Cleans up after aborted sequence
#4) Add genre Metadata
#5) Fix the searching of youtube videos so we get the closest to spotify run time, not just the first that is below 20 seconds


def main():
    #(0)M4A output path, (1)cookie file, (2)ffmpeg, (3)text_file_path,
    settings = EditTextFiles.get_settings('C:\\Users\\eliza\\OneDrive\\Documents\\Desktop\\iPod\\settings\\settings.txt')
    text_file_path = settings[3]
    print('Getting playlist...')
    all_playlists = SpotifyComm.get_playlists()
    all_playlists = SpecificPlaylistSelection.select(all_playlists)
    print('Done')
    for playlist_name in all_playlists:
        safe_string = playlist_name[2]
        if exists(text_file_path+'\\'+safe_string) == False:
            open(text_file_path+'\\'+safe_string, 'x')
    for x in all_playlists:
        print('Getting '+x[0]+' tracks...')
        playlist = SpotifyComm.get_tracks_in_playlist(x[2])
        safe_string = x[2]
        playlist = EditTextFiles.edit_text_files(playlist, text_file_path+'\\'+safe_string)
        print('Done')
        print('Searching YouTube, Downloading M4A...')
        for y in playlist:
            safe_song_title = y[0]
            if '/' in safe_song_title:
                safe_song_title = safe_song_title.replace('/', '--')
            video_id = YouTubeComm.get_videos(safe_song_title+' '+y[1]+' lyrics', y[3], settings[1])
            bad_download = True
            while bad_download:
                bad_download = YouTubeComm.download_audio(video_id,
                                                          safe_string, safe_song_title, settings[0], settings[1], settings[2])
            safe_song_title = Tagging.safe_string(safe_song_title)
            directory = settings[0]+safe_string+'\\'+safe_song_title+'.m4a'
            Tagging.metadata(directory, SpotifyComm.get_metadata(y[2]))
        print('Done')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
