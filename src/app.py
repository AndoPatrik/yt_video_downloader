import customtkinter as ctk
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


# General settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("../static/custom_theme.json")

# GUI start point
root = ctk.CTk()
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)

# Logo
logo = Image.open('../static/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = ctk.CTkLabel(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0, columnspan=3)

# YT Link input
link_entry_text = ctk.StringVar()
link_entry = ctk.CTkEntry(
    root, textvariable=link_entry_text, width=300)
link_entry.grid(columnspan=3, column=0, row=1)

# Insturctions
instructions = ctk.CTkLabel(
    root, text="Paste YouTube link and click on download.")
instructions.grid(columnspan=3, column=0, row=2)

# Download button
download_btn_text = ctk.StringVar()
download_btn = ctk.CTkButton(root,
                             textvariable=download_btn_text,
                             command=lambda: download_button_click())
download_btn_text.set("Download")
download_btn.grid(column=0, row=3, columnspan=3)

# Settings button
settings_button = ctk.CTkButton(root, text='Settings',
                                command=lambda: settings_button_click())
settings_button.grid(column=0, row=4, columnspan=3)

# Run the GUI main loop
root.mainloop()
í
