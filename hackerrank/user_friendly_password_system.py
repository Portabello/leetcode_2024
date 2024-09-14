#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
import string
additions = [""]+list(string.ascii_letters)+[str(d) for d in range(10)]

def authEvents(events):
    # Write your code here
    #print(additions)
    valid = []
    ans = []
    for event in events:
        if event[0] == 'setPassword':
            valid = []
            for x in additions:
                valid.append(hashString(event[1]+x))
            #print(valid)
        elif event[0] == 'authorize':
            #print(valid)
            if int(event[1]) in valid:
                ans.append(1)
            else:
                ans.append(0)
    return ans

def hashString(str):
    t = 0
    power = len(str)-1
    for x in str:
        t+=ord(x)*(131**power)
        power -=1
    return t % ((10**9)+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
