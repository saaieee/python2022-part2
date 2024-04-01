
from song import Song
from songcollection import SongCollection


def run_tests():
    """Testing songcollection class."""

    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs

    print("Test loading songs:")
    song_collection.load_songs('songs.csv')
    print(song_collection)
    assert song_collection.songs

    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    """ Testing sorting songs """
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)
    # TODO: Add more sorting tests
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)

    # TODO: Test saving songs (check CSV file manually to see results)
    print("Test - saving songs")
    song_collection.save_in_csv("songs.csv")

    # TODO: Add more tests, as appropriate, for each method
    print("Learned songs: {}".format(song_collection.get_unlearned_songs()))
    print("Unlearned songs: {}".format((song_collection.get_learned_songs())))


run_tests()
