#!/bin/python3

import math
import os
import random
import re
import sys

def formula(s, t):
    l = len(s)
    c = 0
    for i in range(len(t) - l +1):
        if s == t[i: i+l]:
            c += 1
    return l * c

# Complete the maxValue function below.
def maxValue(t):
    l = len(t)
    max = 0
    store = []
    for i in range(1, l+1):
        for j in range(l-i+1):
            subs = t[j: j+i]
            if subs in store:
                continue
            store.append(subs)
            val = formula(subs, t)
            max = val if max < val else max
    return max

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
