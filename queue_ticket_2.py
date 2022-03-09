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
    while tickets[p] > 0:

        if 0 in tickets:
            if 0 in tickets[:p+1]:
                p -= 1
            tickets.remove(0)

        if tickets[p] == 1:
            total += len(tickets[:p+1])
            print(tickets)
            break
    
        print(tickets) 
        tickets = list(map(lambda x: x-1, tickets))
        total += len(tickets)

    return total
       

if __name__ == '__main__':
    tickets = list(map(int, sys.argv[2:]))
    p = int(sys.argv[1])
    # tickets = [4, 6, 3, 6, 5]
    # p = 2
    result = waitingTime(tickets, p)
    print(result)
