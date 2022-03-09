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


# So, the idea here is that

# All the people before tickets[p] will go the
# minimum of their ticket and tickets[p]

# All the people after tickets[p] will go their 
# "ticket number - 1" or just their "ticket number"
# if it is less than ticket[p] 

def waitingTime(tickets, p):
    # Write your code here
    total = 0
    for pos, ticket in enumerate(tickets):
        total += min(ticket, (tickets[p] - (tickets[p] > pos)))

    return total
       

if __name__ == '__main__':
    tickets = list(map(int, sys.argv[2:]))
    p = int(sys.argv[1])
    # tickets = [4, 6, 3, 6, 5]
    # p = 2
    result = waitingTime(tickets, p)
    print(result)
