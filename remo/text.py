import tkinter as tk

def main():
    # Function to change the label text by adding one
    def increase():
        lbl.configure(text=int(lbl.cget("text")) + 1)

    # Function to change the label text by subtracting one
    def decrease():
        lbl.configure(text=int(lbl.cget("text")) - 1)

    # Function to reset the label text
    def reset():
        lbl.configure(text="0")

    # Create a new window
    window = tk.Tk()

    # Set window size and position
    window.geometry("250x250")

    # Create label and buttons
    lbl = tk.Label(master=window, text="0")
    btn_decrease = tk.Button(master=window, text="-", command=decrease)
    btn_increase = tk.Button(master=window, text="+", command=increase)
    btn_reset = tk.Button(master=window, text="Reset", command=reset)

    # Pack the label and buttons
    btn_decrease.pack(side="left", fill=tk.BOTH, expand=True)
    lbl.pack(side="left", fill=tk.BOTH, expand=True)
    btn_increase.pack(side="left", fill=tk.BOTH, expand=True)
    btn_reset.pack(side="left", fill=tk.BOTH, expand=True)

    # Start event loop
    window.mainloop()

# Call main function
main()
