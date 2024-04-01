"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class

from song import Song
from songcollection import SongCollection


def add_song(my_songs):
    title = song_title()
    artist = song_artist()
    year = song_year()
    print(f"{title} by {artist} ({year}) added to song list")
    my_songs.add_song(Song(title, artist, year, is_learned=False))


def song_title():
    title = input("Title: ")
    return title.strip()


def song_artist():
    title = input("Title: ")
    return title.strip()


def song_year():
    while True:
        try:
            year = int(input("Year: "))
            if year < 0:  # Making sure the song year is valid
                print("Number must be >= 0")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    return song_year()


def song_list(my_songs):
    songs_learned = my_songs.get_learned_songs()
    songs_unlearned = my_songs.get_unlearned_songs()
    for i, song_data in enumerate(my_songs.songs):
        if song_data.is_learned:
            print("{:1}. * {:45} - {:30} ({})".format(i, song_data.title, song_data.artist, str(song_data.year)))
        else:
            print("{:1}. {:45}   - {:30} ({})".format(i, song_data.title, song_data.artist, str(song_data.year)))
    print("{} Songs learned, {} Songs still to learn ".format(songs_learned, songs_unlearned))


def songs_in_file(my_songs):
    for song in my_songs.songs:
        if not song.is_learned:
            return False
    return True


def song_number(my_songs):
    global learn
    while True:
        try:
            learn = int(input(">>>"))
        except ValueError:
            print("Invalid input.Enter  a  valid number")
            continue
        if learn < 0:
            print("Number must be >= 0")
            continue
        elif learn >= len(my_songs.songs):
            print("Invalid song number")
        else:
            break
    return learn


def learn_song(my_songs):
    if songs_in_file(my_songs):
        print("No songs to learn")
    else:
        print("Enter the number of song to mark as learned")  
        learn = song_number(my_songs)
        song = my_songs.songs[learn]
        if song.is_learned:
            print(f"You have  already learned{song.title}")
        else:
            song.is_learned = True
            print(f"{song.title} by {song.artist} learned")


def main():
    print("Songs to learn 1.0")
    song_collection = SongCollection()
    song_collection.load_songs("songs.csv")
    print(f"{len(song_collection.songs)} songs loaded.")
    while True:
        print("""Menu:
L - List Songs
A - Add a new Songs
C - Complete a Song
Q - Quit""")
        choice = input(">>> ").upper()
        if choice == "L":
            song_collection.sort("title")
            song_list(song_collection)
        elif choice == "A":
            add_song(song_collection)
        elif choice == "W":
            songs_in_file(song_collection)
            learn_song(song_collection)
        elif choice == "Q":
            song_collection.save_in_csv("songs.csv")
            print(f"{len(song_collection.songs)} songs saved to songs.csv")
            break
        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
