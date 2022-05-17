from mutagen.mp4 import MP4


def metadata(directory, dictionary):
    f=MP4(directory)
    f['\xa9nam'] = dictionary['song']
    f['\xa9ART'] = dictionary['artist']
    f['\xa9alb'] = dictionary['album_name']
    f['aART'] = dictionary['album_artist']
    f['desc'] = str(dictionary['song_track'])+'/'+str(dictionary['album_tracks'])+'  '+str(dictionary['album_disc'])
    f['\xa9day'] = dictionary['year']
    if dictionary['compilation'] == 'compilation':
        f['cpil'] = True
    else:
        f['cpil'] = False

    f['\xa9gen'] = dictionary['genre']
    f.save()