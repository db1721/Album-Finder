from youtubesearchpython import VideosSearch
from download_audio import DownloadAudio
from find_songs_from_album import FindSongs


class Run:
    def __init__(self, band_and_album_to_search_for):
        """
        # Step 1 - Enter the artist and album
        # Step 2 - Retrieve all songs with title and duration
        # Step 3 - For each song, search for YouTube video with same duration and most views
        # Step 4 - Download from the YouTube link
        :param band_and_album_to_search_for:
        """
        self.band_and_album_to_search_for = band_and_album_to_search_for
        band_album = self.band_and_album_to_search_for.split('-')
        self.artist = band_album[0].strip()
        self.album = band_album[1].strip()
        self.songs = FindSongs(self.artist, self.album)
        self.song_list = []

    def execute_main(self):
        """

        :return:
        """
        # Step 1 - Enter the artist and album

        # Step 2 - Retrieve all songs with title and duration
        self.get_album_list()
        # Step 3 - For each song, search for YouTube video with same duration and most views
        # Using simple list now. Need to use detailed list to compare times
        self.download_link()
        # Step 4 - Download from the YouTube link
        # Step 5 - Rename file

    def get_album_list(self):
        """
        Calls the FindSongs class to get a list of songs
        :return:
        """
        self.songs.make_song_list()
        self.song_list = self.songs.simple_album_details
        print(self.songs.simple_album_details)

    def download_link(self):
        """
        From list, downloads all songs
        :return:
        """
        band_album = self.band_and_album_to_search_for.split('-')
        artist = band_album[0]
        album = band_album[1]
        download = DownloadAudio(self.artist, self.album)
        count = 1

        for count, song in enumerate(self.song_list):
            song_to_search_for = f'{self.artist} - {song}'

            videosSearch = VideosSearch(song_to_search_for, limit=1)

            yt_title = ''
            song_duration = ''
            artist_name = ''
            duration = ''

            for key, value in videosSearch.result().items():
                for video_data in value:
                    print(f'Video {count}: {song_to_search_for}')
                    for key2, value2 in video_data.items():
                        # print(f'{key2}: {value2}')
                        if key2 == 'duration':
                            duration = value2
                            print(f'    {key2}: {value2}')
                        if key2 == 'title':
                            yt_title = value2
                            print(f'    {key2}: {value2}')
                        if key2 == 'link':
                            print(f'    {key2}: {value2}')
                            download.download(value2, song, yt_title, count, duration)
                    count += 1


execute = Run('SECRETS - The Collapse')
execute.execute_main()
