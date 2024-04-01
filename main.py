
# TODO: Create your main program in this file, using the SongsToLearnApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from song import Song
from songcollection import SongCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty

CATEGORIES = {'Title': 'title', 'Year': 'year', 'Artist': 'artist', 'Learned': 'is_learned'}
FILENAME = 'songs.csv'


class SongsToLearnApp(App):
    """to create a GUI for our APP """
    current_value = StringProperty()
    categories = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.song_collection.load_songs(FILENAME)

    def build(self):
        self.title = "Songs to listen to "
        self.root = Builder.load_file('app.kv')
        self.categories = sorted(CATEGORIES.keys())
        self.current_value = self.categories[0]
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creating widget for the GUI"""
        self.root.ids.entries_box.clear_widgets()
        for song in self.song_collection.songs:
            temp_button = Button(text=str(song))
            if song.is_learned:
                temp_button.background_color = (1, 0, 1, 1)
            else:
                temp_button.background_color = (1, 0, 0, 0)
            temp_button.bind(on_release=self.press_entry)
            temp_button.song = song
            self.root.ids.entries_box.add_widget(temp_button)
            self.root.ids.status_text.text = f'For learning: {self.song_collection.get_unlearned_songs()}. ' \
                                             f'Learned: {self.song_collection.get_learned_songs()} '

    def press_entry(self, instance):

        song = instance.song
        if song.is_unlearned:
            song.unlearned_songs()
            self.root.ids.output_label.text = f'You need to learn {song.title}'
            instance.background_color = (0, 0, 1, 1)
        else:
            song.is_learned()
            self.root.ids.output_label.text = f'You have already learned {song.title}'
            instance.background_color = (1, 0, 0, 1)
        self.root.ids.status_text.text = f'To learn: {self.song_collection.get_unlearned_songs()}. Learned: ' \
                                         f'{self.song_collection.get_learned_songs()} '
        self.sort_songs(self.root.ids.values_to_sort.text)

        instance.text = str(song)

    def add_song(self):
        """To add new songs to the list"""
        title = str(self.root.ids.title_input.text)
        artist = str(self.root.ids.artist_input.text)
        try:
            year = int(self.root.ids.year_input.text)
            if year < 0:
                self.root.ids.year_input.text = "Number must be >= 0"
                return False
        except ValueError:
            self.root.ids.output_label.text = "You must enter a valid number"
            return False
        if title == "" or artist == "" or year == "":
            self.root.ids.output_label.text = "All fields must be completed"
            return False
        new_song = Song(title, artist, year, False)
        self.song_collection.add_song(new_song)
        self.sort_songs(self.root.ids.values_to_sort.text)

    def sort_songs(self, value):
        self.song_collection.sort(CATEGORIES[value])
        self.create_widgets()

    def clear_all(self):
        self.root.ids.title_input.text = ''
        self.root.ids.output_label.text = ''
        self.root.ids.artist_input.text = ''
        self.root.ids.status_text.text = ''
        self.root.ids.year_input.text = ''

    def on_stop(self):
        """To save the songs if the user quits"""
        self.song_collection.save_in_csv(FILENAME)


if __name__ == '__main__':
    SongsToLearnApp().run()
