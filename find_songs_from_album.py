import musicbrainzngs
from utilities.time_conversion import TimeConversion


class FindSongs:
    def __init__(self, artist, album_title):
        """
        Finds songs based on artist and album name provided
        :param artist:
        """
        self.convert_time = TimeConversion()
        self.artist = artist
        self.album_title = album_title
        self.artist_id = ''
        self.album_id = ''
        self.full_album_details = []
        self.simple_album_details = []

        musicbrainzngs.set_useragent("Album Finder App", "0.1", "https://github.com/alastair/python-musicbrainzngs/")

    def make_song_list(self):
        """

        :return: List of songs
        """
        result = musicbrainzngs.search_releases(artist=self.artist, release=self.album_title, limit=1)
        album_id = result["release-list"][0]["id"]

        new_result = musicbrainzngs.get_release_by_id(album_id, includes=["recordings"])
        album_info = (new_result["release"]["medium-list"][0]["track-list"])
        for song in range(len(album_info)):
            song_info = (album_info[song])
            # Options: id, position, title, length
            self.simple_album_details.append(song_info["recording"]["title"])
            print(f'{song_info["number"]}. {song_info["recording"]["title"]}')
                  # f'{self.convert_time.convert_milliseconds_to_time(song_info["length"])}')

    def _get_album_id(self):
        """
        Obtains album id from musicbrainz
        :return:
        """
        try:
            album_dict = musicbrainzngs.get_artist_by_id(self.artist_id,
                                                         includes=["release-groups"],
                                                         release_type=["album", "ep"])
            for key, value in album_dict.items():
                for key2, value2 in value.items():
                    if key2 == 'release-group-list':
                        for item in value2:
                            for key3, value3 in item.items():
                                if key3 == 'id':
                                    self.album_id = value3
                                if key3 == 'title':
                                    if value3.upper() == self.album_title.upper():
                                        raise StopIteration
        except TypeError:
            print(f'{self.album_title} was not found')
            exit('Incorrect Album')
        except StopIteration:
            print(f'{self.album_title} has an ID of {self.album_id}')

    def _get_artist_id(self):
        """
        Obtains artist ID from musicbrainz
        :return:
        """
        try:
            artist_dict = musicbrainzngs.search_artists(self.artist)
            for key, value in artist_dict.items():
                for item in value:
                    for key2, value2 in item.items():
                        if key2 == 'id':
                            self.artist_id = value2
                        if key2 == 'name':
                            if value2.upper() == self.artist.upper():
                                raise StopIteration
        except TypeError:
            print(f'{self.artist} was not found')
            exit('Incorrect Artist')
        except StopIteration:
            print(f'{self.artist} has an ID of {self.artist_id}')

