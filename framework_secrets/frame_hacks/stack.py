
import sys

def one():
    two()

def two():
    three()

def three():
    for i in range(3):
        frame = sys._getframe(i)
        show_frame(i, frame)

def show_frame(num, frame):
    print(frame)
    print(f"frame = sys._getframe({num})")
    print(f"function = {frame.f_code.co_name}")
    print("\n")

one()
