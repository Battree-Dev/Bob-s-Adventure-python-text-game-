import tkinter as tk
import subprocess
import threading
import sys
import os

bob_process = None

def read_game_output():
    while True:
        character = bob_process.stdout.read(1)

        if character == "":
            break

        bob_window.after(
            0,
            write_to_output,
            character
        )

def send_input(event=None):
    player_input = game_input.get()

    write_to_output(player_input + "\n")

    bob_process.stdin.write(player_input + "\n")
    bob_process.stdin.flush()

    game_input.delete(0, "end")

def quit_game():
    if bob_process is not None:
        bob_process.terminate()

    bob_window.destroy()

def write_to_output(text):
    game_output.config(state="normal")
    game_output.insert("end", text)
    game_output.see("end")
    game_output.xview_moveto(0)
    game_output.config(state="disabled")


def start_game():
    global bob_process

    game_path = get_game_path()

    bob_process = subprocess.Popen(
        [game_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        creationflags=subprocess.CREATE_NO_WINDOW
        )

    reader_thread = threading.Thread(
        target=read_game_output,
        daemon=True
        )

    reader_thread.start()
#GUI build
bob_window = tk.Tk()
bob_window.title("Battree's First Game: Bob's Adventure.")
bob_window.geometry("1200x800")
bob_window.configure(bg="#181818")
bob_window.protocol("WM_DELETE_WINDOW", quit_game)
outer_frame = tk.Frame(
    bob_window,
    bg="#1b1026",
    padx=15,
    pady=15
    )

outer_frame.pack(
    fill="both",
    expand=True
    )

game_output = tk.Text(
    outer_frame,
    font=("Cascadia Mono", 14),
    bg="#101010",
    fg="#c8c8c8",
    insertbackground="#c8c8c8",
    wrap="none",
    state="disabled"
    )

game_output.pack(
    fill="both",
    expand=True
    )

seperator = tk.Frame(
    outer_frame,
    height=2,
    bg="#49305f"
    )
seperator.pack(
    fill="x",
    pady=(8, 8)
    )

input_row = tk.Frame(
    outer_frame,
    bg="#181818"
    )
input_row.pack(fill="x")

game_input = tk.Entry(
    input_row,
    font=("Comic Sans MS", 14),
    bg="#202020",
    fg="#e0e0e0",
    insertbackground="#e0e0e0"
    )
game_input.pack(
    side="left",
    fill="x",
    expand=True
    )
game_input.focus_set()
game_input.bind("<Return>", send_input)

quit_button = tk.Button(
    input_row,
    text="Quit Game",
    bg="#303030",
    fg="#d0d0d0",
    command=quit_game
    )
quit_button.pack(
    side="right",
    padx=(10, 0)
    )

def get_game_path():
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, "BobsAdventure.exe")
    else:
        return os.path.join("dist", "BobsAdventure.exe")


start_game()

bob_window.mainloop()