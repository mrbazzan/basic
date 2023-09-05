from tkinter import *  # Python 3
import turtle

#
# using ghostscript to convert from .eps to .png
# gs -dSAFER -dEPSCrop -r300 -sDEVICE=jpeg -o <.png> <.eps>
# sshotwell image.png
#

def three_colored_flag(first_colour,
                       second_colour,
                       third_colour,
                       filename=None):
    pen = turtle.Turtle()
    def rectangle(colour):
        for i in range(2):
            pen.begin_fill()
            pen.fillcolor(colour)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
            pen.rt(90)
            pen.end_fill()
    pen.pensize(4)
    pen.penup()
    pen.goto(0,-200)
    pen.pendown()
    pen.left(90)
    pen.forward(400)
    pen.right(90)
    rectangle(first_colour)
    pen.forward(50)
    rectangle(second_colour)
    pen.forward(50)
    rectangle(third_colour)
    pen.forward(50)
    pen.hideturtle()

    if filename:
        ts = turtle.getscreen()
        file_extension = filename.split('.')
        filename = file_extension[0] + ".eps"
        ts.getcanvas().postscript(file=filename)


# Draw the Nigerian flag
name = "flag.eps"
three_colored_flag("green","white","green", name)


import pathlib

file_name = "flag.eps"
print(f"The size of the file is: {pathlib.Path(name).stat().st_size}B")
