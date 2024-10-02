
import sys, re
from string import Template

def getchunks(s):
    matches = list(re.finditer(r"\$\{(.*?)\}", s))
    if matches:
        pos = 0
        for match in matches:
            yield s[pos : match.start()]
            yield [match.group(1)]
            pos = match.end()
        yield s[pos:]

def interpolate(templateStr):
    prev_frame = sys._getframe(1)
    result = ""
    for chunk in getchunks(templateStr):
        if type(chunk) is str:
            result += chunk
        else:
            result += eval(*chunk, prev_frame.f_locals)

    return result


name = 'Guido van Rossum'
places = 'Amsterdam', 'LA', 'New York', 'DC', 'Chicago',

s = """My name is ${'Mr. ' + name + ', Esquire'}.

I have visited the following cities:  ${', '.join(places)}.
"""

if __name__ == "__main__":
    print(interpolate(s))

