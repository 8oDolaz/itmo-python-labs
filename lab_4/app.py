import config
from key_generation import generate_key

from pygame import mixer
import tkinter as tk

def mixer_controller():
    mixer.init()
    mixer.music.load(config.background_music)
    mixer.music.set_volume(config.music_volume)
    mixer.music.play(-1)

def display_key():
    key_bg = tk.Canvas(
        root,
        width=250, height=35,
        highlightbackground='cadetblue3',
        bg='cornflowerblue',
    )
    key_bg.create_text(
        125, 20,
        text=generate_key(),
        font=config.font,
        fill='black'
    )
    key_bg.pack()
    key_bg.place(x=120, y=315)

def main():
    root.title(config.window_name)
    root.geometry(config.window_size)
    root.resizable(False, False)

    mixer_controller()

    background_image = tk.PhotoImage(file=config.background_image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    greeting = tk.Canvas(
        root,
        width=550, height=84,
        highlightbackground='cadetblue3',
        bg='cadetblue4',
    )
    greeting.create_text(
        250, 42,
        text=message,
        font=config.font,
        fill='black',
    )
    greeting.pack()
    greeting.place(x=220, y=15)

    generate_button = tk.Button(
        root,
        command=display_key,
        text=config.button_text,
        font=config.font,
        activebackground='chartreuse3',
        bg='cadetblue3'
    )
    generate_button.place(x=468, y=300)

    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    message = config.greeting_message

    main()
