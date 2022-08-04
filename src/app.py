import customtkinter as ctk
import download
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk

# Event handlers


def download_button_click():
    link = link_entry.get()
    if link:
        download.download(link)
    else:
        print("Error: Missing YT link")


def radiobutton_event():
    print("radiobutton toggled, current value:", settings_radio_var.get())


def path_button_event():
    filename = askdirectory()
    download.output_path = filename
    path_label_text.set("Save to: {0}".format(download.output_path))


# General settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("../static/custom_theme.json")

# GUI start point
root = ctk.CTk()
root.title("YT video downloader")
root.geometry("400x500")
root.resizable(False, False)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

# Logo
logo = Image.open('../static/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = ctk.CTkLabel(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0, columnspan=4, pady=20)

# Settings radio buttons
settings_radio_var = ctk.IntVar()

settings_radiobutton_audio = ctk.CTkRadioButton(master=root, text="Only audio",
                                                command=radiobutton_event, variable=settings_radio_var, value=1)
settings_radiobutton_video = ctk.CTkRadioButton(master=root, text="Only video",
                                                command=radiobutton_event, variable=settings_radio_var, value=2)
settings_radiobutton_both = ctk.CTkRadioButton(master=root, text="Video and audio",
                                               command=radiobutton_event, variable=settings_radio_var, value=3)

settings_radiobutton_audio.grid(column=0, row=1, padx=10)
settings_radiobutton_video.grid(column=1, row=1, padx=10)
settings_radiobutton_both.grid(column=2, row=1, padx=10)

# YT Link input
link_entry_text = ctk.StringVar()
link_entry = ctk.CTkEntry(
    root, textvariable=link_entry_text, width=300, placeholder_text="Paste YT link here")
link_entry.grid(columnspan=4, column=0, row=2, pady=20)

# Path
path_label_text = ctk.StringVar(
    value="Save to: {0}".format(download.output_path))
path_label = ctk.CTkLabel(
    root, textvariable=path_label_text)
path_label.grid(columnspan=3, column=0, row=3)

path_button = ctk.CTkButton(
    root, text='Browse', width=50, command=lambda: path_button_event())
path_button.grid(column=0, row=4, columnspan=4)


# Download button
download_btn_text = ctk.StringVar()
download_btn = ctk.CTkButton(root,
                             textvariable=download_btn_text,
                             command=lambda: download_button_click())
download_btn_text.set("Download")
download_btn.grid(column=0, row=5, columnspan=4, pady=30)

# Config elements
settings_radiobutton_both.select()

# Run the GUI main loop
root.mainloop()
