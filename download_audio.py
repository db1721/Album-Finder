import mutagen
from pytube import YouTube
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from album_directory.albums_saved_here import AlbumsSavedDirectory


class DownloadAudio:
    def __init__(self, artist, album):
        """
        Downloads from links provided
        :param artist:
        """
        self.save_directory = AlbumsSavedDirectory()
        self.artist = artist
        self.album = album

    def download(self, link_to_download, song_title, yt_song_title, song_number, song_length):
        """
        Downloads from YouTube links provided
        :param song_length:
        :param song_number:
        :param link_to_download:
        :param song_title:
        :param yt_song_title:
        :return:
        """
        yt = YouTube(link_to_download)

        video = yt.streams.filter(only_audio=True).first()
        folder_build = f'{self.artist} - {self.album}'

        # Save location
        downloads_path = self.save_directory.get_save_directory(folder_build)
        out_file = video.download(output_path=downloads_path)

        base, ext = os.path.splitext(out_file)
        new_base = base.replace(yt_song_title, f'{song_title}')
        new_file = new_base + f'.mp4'
        os.rename(out_file, new_file)

        try:
            audio = EasyID3(new_file)
        except mutagen.id3.ID3NoHeaderError:
            audio = mutagen.File(new_file, easy=True)
            audio.add_tags()

        audio['title'] = song_title
        audio['artist'] = self.artist
        audio['album'] = self.album
        # audio['composer'] = self.artist
        audio['copyright'] = u''
        # audio['encodedby'] = u''
        # audio['length'] = song_length
        audio['tracknumber'] = str(int(song_number) + 1)
        audio.save()
