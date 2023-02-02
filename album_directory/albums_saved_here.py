import os


class AlbumsSavedDirectory:
    def __init__(self):
        self._save_directory = os.path.dirname(__file__)

    def get_save_directory(self, artist_album_name):
        """
        Provides the directory where main files reside
        :return: Directory where main files reside
        """
        try:
            os.mkdir(os.path.join(self._save_directory, artist_album_name))
        except FileExistsError:
            pass
        return os.path.join(self._save_directory, artist_album_name)
