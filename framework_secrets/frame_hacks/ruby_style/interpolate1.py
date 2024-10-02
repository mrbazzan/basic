
import sys
from string import Template

def interpolate(templateStr):
    prev_frame = sys._getframe(1)
    d = prev_frame.f_locals

    t = Template(templateStr)
    return t.substitute(**d)

name = 'Feihong'
place = 'Chicago'
print(interpolate("My name is ${name}. I work in ${place}."))

