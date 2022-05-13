from mutagen.mp4 import MP4


def metadata(directory, dictionary):
    f=MP4(directory)
    f['\xa9nam'] = 'u'+dictionary['song']
    f['\xa9ART'] = 'u'+dictionary['artist']
    f['\xa9alb'] = 'u'+dictionary['album_name']
    f['aART'] = 'u'+dictionary['album_artist']
    f['desc'] = 'u'+dictionary['song_tracks']+'/'+dictionary['album_tracks']+'  '+dictionary['album_disc']
    f['\xa9day'] = 'u'+dictionary['year']
    if dictionary['compilation'] == 'compilation':
        f['cpil'] = False
    else:
        f['cpil'] = True
    if dictionary['genre'] != None:
        f['\xa9gen'] = dictionary['genre'][0]
    f.save()