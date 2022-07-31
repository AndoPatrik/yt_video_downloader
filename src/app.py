import tkinter as tk
from pytube import YouTube
from distutils import text_file
from turtle import clear
from PIL import Image, ImageTk

# Functions


def download(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download()


def download_button_click():
    print(link_entry.get())
    link = link_entry.get()
    if link:
        download(link)
    else:
        print("Error: Missing YT link")


# GUI start point
root = tk.Tk()

# Grid setup
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)

# Logo
logo = Image.open('../static/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# YT Link input
link_entry_text = tk.StringVar()
link_entry = tk.Entry(root, textvariable=link_entry_text, width=80)
link_entry.grid(columnspan=3, column=0, row=1)

# Insturctions
instructions = tk.Label(root, text="Paste YouTube link and click on download.")
instructions.grid(columnspan=3, column=0, row=2)

# Download button
download_btn_text = tk.StringVar()
download_btn = tk.Button(root,
                         textvariable=download_btn_text,
                         command=lambda: download_button_click())
download_btn_text.set("Download")
download_btn.grid(column=1, row=3)

# Run the GUI main loop
root.mainloop()
