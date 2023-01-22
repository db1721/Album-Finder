from pytube import YouTube
import os
from pathlib import Path


class DownloadAudio:
    def __init__(self, artist):
        """

        :param artist:
        """
        self.artist = artist

    def download(self, link_to_download, song_title, yt_song_title):
        """

        :param link_to_download:
        :param song_title:
        :param yt_song_title:
        :return:
        """
        yt = YouTube(link_to_download)

        video = yt.streams.filter(only_audio=True).first()

        # Save location
        downloads_path = str(Path.home() / "Downloads")
        out_file = video.download(output_path=downloads_path)

        base, ext = os.path.splitext(out_file)
        new_base = base.replace(yt_song_title, f'{self.artist} - {song_title}')
        new_file = new_base + f'.mp4'
        os.rename(out_file, new_file)
