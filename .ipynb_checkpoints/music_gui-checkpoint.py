import tkinter as tk
from tkinter import messagebox
import os

MIDI_FILE = "generated_music.mid"

# ---------------- Functions ---------------- #

def play_music():
    if os.path.exists(MIDI_FILE):

        os.startfile(MIDI_FILE)

        status_label.config(
            text="🎵 Playing AI Generated Music...",
            fg="#00FF7F"
        )

    else:

        messagebox.showerror(
            "Error",
            "generated_music.mid not found!"
        )

def open_file():

    if os.path.exists(MIDI_FILE):

        os.startfile(MIDI_FILE)

    else:

        messagebox.showerror(
            "Error",
            "File not found!"
        )

def exit_app():

    root.destroy()


# ---------------- Window ---------------- #

root = tk.Tk()

root.title("AI Music Generator")
root.geometry("800x500")
root.configure(bg="#1E1E2E")
root.resizable(False, False)

# ---------------- Header ---------------- #

title = tk.Label(
    root,
    text="🎵 AI Music Generation Using LSTM Neural Networks",
    font=("Segoe UI", 18, "bold"),
    bg="#1E1E2E",
    fg="#00D4FF"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Generate and Play AI-Composed Music",
    font=("Segoe UI", 11),
    bg="#1E1E2E",
    fg="white"
)

subtitle.pack()

# ---------------- File Info ---------------- #

if os.path.exists(MIDI_FILE):

    file_size = round(
        os.path.getsize(MIDI_FILE) / 1024,
        2
    )

    file_info = f"MIDI File Size : {file_size} KB"

else:

    file_info = "MIDI File Not Found"

info_label = tk.Label(
    root,
    text=file_info,
    font=("Segoe UI", 11, "bold"),
    bg="#1E1E2E",
    fg="#FFD700"
)

info_label.pack(pady=15)

# ---------------- Buttons ---------------- #

frame = tk.Frame(
    root,
    bg="#1E1E2E"
)

frame.pack(pady=40)

play_btn = tk.Button(
    frame,
    text="▶ Play Music",
    command=play_music,
    bg="#28A745",
    fg="white",
    width=18,
    height=2,
    font=("Segoe UI", 11, "bold"),
    relief="flat"
)

play_btn.grid(
    row=0,
    column=0,
    padx=10
)

open_btn = tk.Button(
    frame,
    text="📂 Open MIDI",
    command=open_file,
    bg="#007BFF",
    fg="white",
    width=18,
    height=2,
    font=("Segoe UI", 11, "bold"),
    relief="flat"
)

open_btn.grid(
    row=0,
    column=1,
    padx=10
)

exit_btn = tk.Button(
    frame,
    text="❌ Exit",
    command=exit_app,
    bg="#DC3545",
    fg="white",
    width=18,
    height=2,
    font=("Segoe UI", 11, "bold"),
    relief="flat"
)

exit_btn.grid(
    row=0,
    column=2,
    padx=10
)

# ---------------- Status ---------------- #

status_label = tk.Label(
    root,
    text="Ready",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2E",
    fg="white"
)

status_label.pack(pady=25)

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Developed by Saravanan | AI Internship Project 2026",
    font=("Segoe UI", 9),
    bg="#1E1E2E",
    fg="#AAAAAA"
)

footer.pack(side="bottom", pady=15)

root.mainloop()