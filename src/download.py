import os
from pytube import YouTube

output_path = os.getcwd()
only_audio = False
only_video = False


def download(link):
    yt = YouTube(link)

    yd = yt.streams.get_highest_resolution()

    if only_audio:
        yd = yt.streams.get_audio_only()

    if only_video:
        yd = yt.streams.filter(only_video=True)  # TODO: Fix

    yd.download(output_path)
