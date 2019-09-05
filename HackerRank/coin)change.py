#!/bin/python3

import math
import os
import random
import re
import sys

def sort(n):
    for i in range(n):
        for j in range(n-1):
            if n[j] > n[j+1]:
                n[j] = n[j] + n[j+1]
                n[j+1] = n[j] - n[j+1]
                n[j] = n[j] - n[j+1]
    return n

# Complete the getWays function below.
def getWays(n, c, count):
    for i in range(len(c)):
        if n - c[i] >= 0:
            if n - c[i] == 0:
                count += 1
            print('count is', count, ' c[i] is', c[i])
            getWays(n - c[i], c, count)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c, 0)
    print('ways is', ways)

    # fptr.close()
