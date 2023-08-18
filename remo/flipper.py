import random
import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Color Flipper")
    root.geometry("800x600")

    def flip_colors():
        colors = ["red", "green", "blue", "yellow", "orange"]
        label.configure(background=random.choice(colors))

    def set_color_to_red():
        label.configure(background="red")

    def set_color_to_blue():
        label.configure(background="blue")


    label = tk.Label(
        root,
        text="Click to flip colors",
        height=10, width=60,
        bd=2, relief=tk.RAISED
    )
    label.grid(row=0, column=1, padx=10, pady=10)

    button = tk.Button(
        root,
        text="Flip Colors", command=flip_colors
    )
    button.grid(row=1, column=1, padx=10, pady=10)

    button1 = tk.Button(
        root,
        text="Set Color to Red", command=set_color_to_red
    )
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2 = tk.Button(
        root, text="Set Color to Blue",
        command=set_color_to_blue
    )
    button2.grid(row=1, column=2, padx=10, pady=10)

    root.mainloop()

create_gui()
