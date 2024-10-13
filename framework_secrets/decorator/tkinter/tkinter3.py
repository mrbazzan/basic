
from tkinter import Frame, Button, Listbox, END


def bind(widget, event):
    def decorator(func):
        widget.bind(event, func)
        return func
    return decorator


if __name__ == "__main__":
    frame = Frame()
    frame.master.title("Event binding with decorators")
    frame.pack()

    lb = Listbox(frame, name='lb')
    for s in ['one', 'two', 'three', 'four']:
        lb.insert(END, s)
    lb.pack()

    @bind(lb, '<<ListboxSelect>>')
    def onselect(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(f"You selected item {index}: {value}")

    frame.mainloop()

