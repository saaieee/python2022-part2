
from song import Song
#add import here

def run_tests():
    """Testing song class."""
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    # TODO: Write tests to show this initialisation works
    print (initial_song)
    # TODO: Add more tests, as appropriate, for each method
    initial_song = Song("chennai express", "kattappa", 2016, False)
    initial_song.learned_songs()
    print(initial_song)


run_tests()
