"""..."""

from song import Song
from operator import attrgetter


# TODO: Create your SongCollection class in this file


class SongCollection:

    def __init__(self):
        """Initialisng an empty list"""
        self.songs = []

    def __str__(self):
        display_list = []
        for song in self.songs:
            song = f"{song}"
            display_list.append(song)
        return f"{display_list}"

    def sort(self, key):
        self.songs = sorted(self.songs, key=attrgetter(key))

    def add_song(self, song):
        new_song = Song(song.title, song.artist, song.year, song.is_learned)
        self.songs.append(new_song)

    def load_songs(self, filename):
        in_file = open(filename, "r")
        for song in in_file:
            song = song.strip()
            song = song.split(',')
            if song[3] == 'l':
                learn_status = True
            else:
                learn_status = False
            new_song = Song(song[0], song[1], int(song[2]), learn_status)
            self.songs.append(new_song)
        in_file.close()

    def get_learned_songs(self):
        learned_songs = 0
        for song in self.songs:
            if song.is_learned:
                learned_songs += 1
        return learned_songs

    def get_unlearned_songs(self):
        unlearned_songs = 0
        for song in self.songs:
            if not song.is_learned:
                unlearned_songs += 1
        return unlearned_songs

    def save_in_csv(self, songs):
        out_file = open(songs, "w")
        index = 0
        for song in self.songs:
            if song.is_learned:
                print(f"{song.title},{song.artist},{song.year},l", file=out_file)

                index += 1
            else:
                print(f"{song.title},{song.artist},{song.year},u", file=out_file)
                index += 1
        out_file.close()
