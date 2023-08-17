import random
import tkinter as tk


class FlipperApp:

    def __init__(self, master):
        self.root = master
        self.root.title("Color Flipper")
        self.root.geometry("800x600")


    def run(self):

        def flip_colors():
            colors = ["red", "green", "blue", "yellow", "orange"]
            label.configure(background=random.choice(colors))


        label = tk.Label(
            self.root, 
            text="Click to flip colors", 
            height=10, width=60,
            bd=2, relief=tk.RAISED
        )
        label.grid(row=0, column=1, padx=10, pady=10)

        button = tk.Button(
            self.root,
            text="Flip Colors", command=flip_colors
        )
        button.grid(row=1, column=1, padx=10, pady=10)

        self.root.mainloop()


root = tk.Tk()
app = FlipperApp(root)
app.run()

