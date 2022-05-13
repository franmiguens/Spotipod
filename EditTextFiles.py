def edit_text_files(track_list,playlist_path):
    read = open(playlist_path, 'r')
    array = read.('\n')
    read.close()
    write = open(playlist_path, 'w')
    for x in track_list:
        write.write(x[2]+'\n')
        state = False
        for y in array:
            if x==y:
                state=True
        if state == False:
            x.pop()
    write.close()
    return track_list