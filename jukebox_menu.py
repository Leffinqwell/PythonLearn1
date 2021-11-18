from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("please choose your album (invalid choice exits):")
    for index, (title, artits, year, songs) in enumerate(albums):
        print("{}: {}".format(index +1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose a song:")

    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        print("wrong choice")

    print("play {}". format(title))
    print("-" * 40)

    # print(albums[choice - 1])
    # for no, name in songs_list:
    #     print(no, name)