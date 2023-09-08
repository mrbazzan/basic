import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.var = tk.IntVar()

        # Age
        self.age_label = tk.Label(self.root, text="Enter Age: ")
        self.age_entry = tk.Entry(self.root)

        self.age_label.grid(row=1, column=0)
        self.age_entry.grid(row=1, column=1)

        # Gender
        self.gender = tk.Frame(self.root)
        self.gender_male = tk.Radiobutton(
            self.gender, text="Male",
            variable=self.var, value=1
        )
        self.gender_male.pack(side="left")
        self.gender_female = tk.Radiobutton(
            self.gender, text="Female",
            variable=self.var, value=2
        )
        self.gender_female.pack(side="left")
        self.gender.grid(row=2, column=0)

        # Height
        self.height_label = tk.Label(self.root, text="Enter Height (cm): ")
        self.height_entry = tk.Entry(self.root)

        self.height_label.grid(row=3, column=0)
        self.height_entry.grid(row=3, column=1)

        # Weight
        self.weight_label = tk.Label(self.root, text="Enter Weight (kg): ")
        self.weight_entry = tk.Entry(self.root)

        self.weight_label.grid(row=4, column=0)
        self.weight_entry.grid(row=4, column=1)

        self.calculate_button = tk.Button(
            self.root, text="Calculate", command=self.calculate
        )
        self.calculate_button.grid(row=5, column=0)

        self.reset_button = tk.Button(
            self.root, text="RESET", command=self.reset_entry
        )
        self.reset_button.grid(row=5, column=1)

        self.exit_btn = tk.Button(
            self.root, text='Exit',
            command=lambda:self.root.destroy()
        )
        self.exit_btn.grid(row=5, column=2)

    def calculate_bmi(self, age, gender, height, weight):
        bmi = weight / ((height / 100) ** 2)
        return round(bmi, 2)

    @staticmethod
    def display_bmi(bmi):
        if bmi < 18.5:
            messagebox.showinfo(
                'bmi', f'BMI = {bmi} is Underweight')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo(
                'bmi', f'BMI = {bmi} is Normal')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo(
                'bmi', f'BMI = {bmi} is Overweight')
        elif (bmi > 29.9):
            messagebox.showinfo(
                'bmi', f'BMI = {bmi} is Obesity')
        else:
            messagebox.showerror(
                'bmi', 'something went wrong!')

    def calculate(self):
        age = int(self.age_entry.get())
        gender = self.var.get()
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        bmi = self.calculate_bmi(age, gender, height, weight)
        self.display_bmi(bmi)

    def reset_entry(self):
        self.age_entry.delete(0,'end')
        self.height_entry.delete(0,'end')
        self.weight_entry.delete(0,'end')
        self.gender_male.deselect()
        self.gender_female.deselect()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
