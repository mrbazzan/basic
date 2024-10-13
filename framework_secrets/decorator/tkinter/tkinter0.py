
from tkinter import Frame, Button

def onclick():
    print("You clicked a button")


if __name__ == "__main__":
    frame = Frame()
    frame.master.title("Event binding with decorators")
    frame.pack()

    btn1 = Button(frame, text="one")
    btn1.pack()

    btn2 = Button(frame, text="two")
    btn2.pack()

    btn1['command'] = onclick
    btn2['command'] = onclick

    frame.mainloop()

