
import sys, pdb

def test():
    frame = sys._getframe(1)
    pdb.set_trace()

def aFunction():
    a = 1
    b = "hello"
    c = (12, 12.4)
    test()
    d = "This wont show up in the frame"

aFunction()
