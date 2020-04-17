#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestStraightCity function below.
def closestStraightCity(c, x, y, q):
    for i in range(q):
        ind = c.index(q[i])
        







def all_indices(value, qlist):
    indices = []
    idx = -1
    x = 3
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c_count = int(input().strip())

    c = []

    for _ in range(c_count):
        c_item = input()
        c.append(c_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    q_count = int(input().strip())

    q = []

    for _ in range(q_count):
        q_item = input()
        q.append(q_item)

    closestStraightCity(c, x, y, q)

    # fptr.write('\n'.join(res))
    # fptr.write('\n')

    # fptr.close()
