def edit_text_files(track_list, playlist_path):
    open_text = open(playlist_path, 'r')
    read = open_text.read()
    array = read.split('\n')
    open_text.close()
    write = open(playlist_path, 'w')
    tracker = []
    for x in track_list:
        write.write(x[2] + '\n')
        state = True
        for y in array:
            if x[2] == y:
                state = False
        if not state:
            tracker.append(x)
    for x in tracker:
        track_list.remove(x)
    write.close()
    return track_list
