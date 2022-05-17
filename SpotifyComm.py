import spotipy
from spotipy.oauth2 import SpotifyOAuth
import creds

client_id = creds.get_client_id()
client_secret = creds.get_client_secret()
redirect_url = 'http://localhost/'
scope = 'playlist-read-private'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope=scope))

playlists = sp.current_user_playlists()


# For Loop Example
# for x in playlists['items']:
#    print(x)
# print(playlists['items'][0])
# tracks = sp.playlist_items(playlists['items'][0]['id'])
# print(tracks['items'][0]['track'])
# Making txt file
# with open("C:/Users/Fran/Desktop/Testing.txt", 'w') as f:
#    for x in tracks['items']:
#        f.write(x['track']['name'] + " - " + x['track']['artists'][0]['name'] + '\n')


def get_playlists():
    playlists_list = []
    playlists = sp.current_user_playlists()
    for x in playlists['items']:
        playlists_list.append((x['name'], x['tracks']['total'], x['id']))
    return playlists_list


def get_tracks_in_playlist(i):
    tracks = sp.playlist_items(i)
    tracks_arr = []
    for x in tracks['items']:
        tracks_arr.append((x['track']['name'], x['track']['artists'][0]['name'], x['track']['id']))
    return tracks_arr


def get_metadata(i):
    track = sp.track(i)
    metadata = {'song': track['name'],
                'artist': track['artists'][0]['name'],
                'album_name': track['album']['name'],
                'album_artist': track['album']['artists'][0]['name'],
                'album_tracks': track['album']['total_tracks'],
                'album_disc': track['disc_number'],
                'song_track': track['track_number'],
                'year': track['album']['release_date'],
                'genre': 'Incomplete Feature',
                'compilation': track['album']['album_type']
                }

    return metadata
