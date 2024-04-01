"""..."""

# TODO: Create your Song class in this file

TRUE = True
FALSE = False


class Song:
    """for creating song objects """

    def __init__(self, title="", artist="", year=0, is_learned=FALSE):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        if self.is_learned:
            return f"{self.title} by {self.artist} ({self.year}) (learned)"
        else:
            return f"{self.title} by {self.artist} ({self.year})"

    def learned_songs(self):
        self.is_learned = TRUE

    def unlearned_songs(self):
        self.is_learned = FALSE
