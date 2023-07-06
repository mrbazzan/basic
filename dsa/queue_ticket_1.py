#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'waitingTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY tickets
#  2. INTEGER p
#

def waitingTime(tickets, p):
    # Write your code here
    total = 0
    while tickets[p] != 0: 
 
        present_value = tickets[0]
        if (present_value-1 > 0):
            tickets.append(present_value - 1)
            tickets.pop(0)
            total += 1
        else:
            total += 1 if (present_value > 0) else 0
            if tickets[p] == 1:
                break
            tickets.remove(present_value)

        p -= 1
        if (p<0):
            p += len(tickets)

    return total
       

if __name__ == '__main__':
    tickets = list(map(int, sys.argv[2:]))
    p = int(sys.argv[1]) 
    result = waitingTime(tickets, p)
    print(result)


