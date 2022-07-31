import tkinter as tk
import settings_window
import download
from PIL import Image, ImageTk

# Event handlers


def download_button_click():
    link = link_entry.get()
    if link:
        download.download(link)
    else:
        print("Error: Missing YT link")


def settings_button_click():
    settings_window.display(root)


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

# Settings button
settings_button = tk.Button(root, text='Settings',
                            command=lambda: settings_button_click())
settings_button.grid(column=2, row=3)

# Run the GUI main loop
root.mainloop()
