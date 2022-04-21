import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id='8586a99fc7a64e3d95e699fe47bd7978'
client_secret='f90cc5d7395647b7a8890afdf2dd40f2'
redirect_url='http://localhost/'
scope = 'playlist-read-private'

sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope=scope))

playlists = sp.current_user_playlists()

#For Loop Example
#for x in playlists['items']:
#    print(x)
print(playlists['items'][0])
tracks = sp.playlist_items(playlists['items'][0]['id'])
print(tracks['items'][0]['track'])
#Making txt file
#with open("C:/Users/Fran/Desktop/Testing.txt", 'w') as f:
#    for x in tracks['items']:
#        f.write(x['track']['name'] + " - " + x['track']['artists'][0]['name'] + '\n')


def get_playlists():
    playlists_list = []
    playlists = sp.current_user_playlists()
    for x in playlists['items']:
        description = [x['name'], get_tracks_in_playlist(x)]
        playlists_list.append(description)
    return playlists_list


def get_tracks_in_playlist(x):
    tracks = sp.playlist_items(x['id'])
    tracksArr = []
    for y in tracks['items']:
        tracksArr.append(y['track']['name'])
        tracksArr.append(y['track']['artists'][0]['name'])
        tracksArr.append(y['track']['id'])
    return tracksArr


#def get_metadata():
