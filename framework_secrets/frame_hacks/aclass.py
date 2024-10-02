
import sys, pdb

def test():
    frame = sys._getframe(1)
    pdb.set_trace()

class Test:
    a = 1
    b = "hello"
    c = (12, 3.45)
    test()
    d = "This won't show"
