import lyricsgenius

class FindSongs:
    def __init__(self, artist, album_title):
        """

        :param artist:
        """
        token = 'qg2MbKFbMrqL96Sd7LAUqwy8jrYIVM0Z5JAmH0z9mwYx7EspqDrVTAgCtZLOn2n8'
        self.artist = artist
        self.album_title = album_title
        self.genius = lyricsgenius.Genius(token)

    def make_song_list(self):
        """

        :return: List of songs
        """
        album_list = self.genius.search_album(name=self.album_title, artist=self.artist)
        another_album_list = album_list.tracks
        print(another_album_list)
