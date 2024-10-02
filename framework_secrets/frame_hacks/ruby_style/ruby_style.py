
import sys

from string import Template
from datetime import datetime

from interpolate2 import getchunks

numbers = [-3, 5, 66, 12, 76]
startTime = datetime(2008, 1, 16, 16, 4)
endTime = datetime(2008, 3, 13, 9, 30, 0)

def interpolate(s):
    prev_frame = sys._getframe(1)
    result = ""
    for chunk in getchunks(s):
        if isinstance(chunk, list):
            # NB: `eval` uses `prev_frame` implicitly because it is
            # contained in locals()
            result += str(eval(chunk[0]))
        else:
            result += chunk
    return result


print(interpolate("Took ${(endTime-startTime).seconds} seconds "\
                  "to get an average of ${(sum(numbers)/len(numbers))}"))

