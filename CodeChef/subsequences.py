# from itertools import combinations
# t=int(input())
# while t!=0:
#     t=t-1
#     n, k = [int(x) for x in input().strip().split(" ")]

#     arr = [int(i) for i in input().split()]
#     comb = list(combinations(arr, k))
#     minEg = sum(comb[0])
#     c=0
#     for i in range(1, len(comb)):
#         egX = sum(comb[i])
#         if egX < minEg:
#             minEg=egX
#     # instances
#     for i in range(len(comb)):
#         if minEg == sum(comb[i]):
#             c=c+1
#     print(c)    

# cook your dish here
# from itertools import combinations
# t=int(input())
# while t!=0:
#     t=t-1
#     n, k = [int(x) for x in input().strip().split(" ")]

#     arr = [int(i) for i in input().split()]
#     comb = list(combinations(arr, k))
#     comb.sort(key = sum)
#     minEg = sum(comb[0])
#     c = 1
#     for i in range(1, len(comb)):
#         egX = sum(comb[i])
#         if egX == minEg:
#             c=c+1
#         if egX > minEg:
#             break
        
#     print(c)       

# cook your dish here
from itertools import combinations
t=int(input())
while t!=0:
    t=t-1
    n, k = [int(x) for x in input().strip().split(" ")]

    arr = [int(i) for i in input().split()]
    arr.sort()
    # print(arr)
    min = arr[k-1]
    ar = arr[:k]
    for i in range(k, len(arr)):
        if (arr[i] <= arr[k-1]):
            ar.append(arr[i])
        if (arr[i] > arr[k-1]):
            break
    comb = list(combinations(ar, k))
    comb.sort(key = sum)
    minEg = sum(comb[0])
    # print(comb)
    c = 1
    for i in range(1, len(comb)):
        egX = sum(comb[i])
        if egX == minEg:
            c=c+1
        if egX > minEg:
            break
        
    print(c)    