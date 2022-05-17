def select(playlists):
    for x in playlists:
        print(x[0], end=', ')
    print('\n')
    answer = input('Would you like to include all playlists(y/n)')
    if answer == 'y':
        return playlists
    tracker = []
    for x in playlists:
        answer = input('Would you like to include '+x[0]+'(y/n)')
        if answer == 'n':
            tracker.append(x)
    for y in tracker:
        playlists.remove(y)
    return playlists