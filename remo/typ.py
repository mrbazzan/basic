import tkinter
from timeit import default_timer as timer
import random
import string

def speed():
    window = tkinter.Tk()
    window.geometry('600x400')

    config = {}
    config["sentence"] = "This is a random sentence to check speed."
    config["start"] = timer()

    txt_lbl = tkinter.Label(window, text=config.get("sentence"), font='times 20')
    txt_lbl.pack()

    typ_lbl = tkinter.Label(window, text='Start Typing', font='times 20')
    typ_lbl.pack(pady=10)

    entry = tkinter.Entry(window)
    entry.pack()

    def change_text():
       # update the value of "sentence"
       config["sentence"] = ''.join(
            random.choice(string.ascii_uppercase)
            for _ in range(20)
        )
       txt_lbl["text"] = config.get("sentence")

       entry.delete(0, tkinter.END)
       config["start"] = timer()

    def check_result():
        if entry.get() == config.get("sentence"):
            end = timer()
            lbl.configure(text=f'Time: {round((end-config["start"]), 4)}s')
        else:
            lbl.configure(text='Wrong Input')

        entry.delete(0, tkinter.END)
        config["start"] = timer()

    done_btn = tkinter.Button(window, text='Done',
                             command=check_result, width=12, bg='grey')
    done_btn.pack(pady=15)

    again_btn = tkinter.Button(window, text='Try Again',
                             command=change_text, width=12, bg='grey')
    again_btn.pack()

    lbl = tkinter.Label(window, text='', font='times 20')
    lbl.pack(pady=30)

    window.mainloop()

if __name__ == '__main__':
    speed()
