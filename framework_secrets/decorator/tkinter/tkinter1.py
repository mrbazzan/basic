
from tkinter import Frame, Button


class MyButton(Button):
    def command(self, func):
        self['command'] = func
        return func

if __name__ == "__main__":
    frame = Frame()
    frame.master.title("Event binding with decorators")
    frame.pack()

    btn1 = MyButton(frame, text="one")
    btn1.pack()

    btn2 = MyButton(frame, text="two")
    btn2.pack()

    @btn1.command
    @btn2.command
    def onclick():
        print("You clicked a button")

    frame.mainloop()

