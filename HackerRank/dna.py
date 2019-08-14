import math
import os
import random
import re
import sys

n = int(input())
hv = []

healthStr  = input().strip().split(' ')
healthVal  = [int(x) for x in input().split(" ")]

t = int(input())

for i in range(t):
    start, end, str = input().strip().split(' ')
    start, end = [int(start), int(end)]
    hv.append(0)
#     str = input()
    results = 0

    j = start
    while (j <= end):
        results = 0
        sub_len = len(healthStr[j])
        for k in range(len(str) - sub_len + 1):
            if str[k:k+sub_len] == healthStr[j]:
                results += 1
        hv[i] = hv[i] + results*healthVal[j]
        j = j + 1

print (min(hv), " ", max(hv) )