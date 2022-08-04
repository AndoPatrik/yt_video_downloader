import os
from pytube import YouTube

output_path = os.getcwd()


def download(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download(output_path)
