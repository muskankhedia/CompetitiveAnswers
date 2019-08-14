#!/bin/python3

import math
import os
import random
import re
import sys

def getMin(a, b, c):
    # print('a is', a)
    m = 100000000000000
    pos = -1
    for i in range(len(a)):
        if i not in b and not(a[i] < 0):
            if m > a[i]:
                m = a[i]
                pos = i
    return pos

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    mat = [[-1 for i in range(n)] for i in range(n)]
    t = 0
    ans = [-2] * n
    s -=1
    for i in range(len(edges)):
      edges[i][0] -= 1
      edges[i][1] -= 1
    for i in range(n):
        for j in range(n):
            if i != j:
                mat[i][j] = -1
            else:
                mat[i][j] = -1
    # print('*******************')
    for i in range(len(edges)):
      # if i != :
        # print('edges is', edges)
        # print('mat is', mat, '  i ', i)
        # print(mat[edges[i][0]][edges[i][1]])
        mat[edges[i][0]][edges[i][1]] = edges[i][2]
        mat[edges[i][1]][edges[i][0]] = edges[i][2]
    # print('mat is ', mat)
    for i in range(n):
        if i != s:
            ans[i] = mat[s][i]
    read = [-100]
    # print('ans is', ans)
    for c in range(n):
        # print('erad is', read)
        i = getMin(ans, read, s)
        if i == -1:
            break
        # print('get min is', ans[i])
        x = t + ans[i]
        for j in range(n):
            if mat[i][j] != -1  and i != j:
                if ans[j] > (x + mat[i][j]) or ans[j] == -1:
                    # print('j is ', j)
                    ans[j] = (x + mat[i][j])
                    found = False
                    for p in edges:
                        if p[0] == j or p[1] == j:
                            found = True
                            break
                    if found:
                        t = x
                    else:
                        t = 0
                        x = 0
        read.append(i)
    for i in range(n):
        if i != s:
            print(ans[i], end=' ')
    print()



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
