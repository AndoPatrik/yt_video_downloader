from pytube import YouTube


def download(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download()
