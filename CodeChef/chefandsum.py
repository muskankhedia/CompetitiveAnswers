def chefandsum():
    n, k = [int(x) for x in input().strip().split(" ")]
    arr = [int(i) for i in input().split()]
    for i in range(n):
        for j in range(n):
            if (i != j):
                if arr[i] + arr[j] == k:
                    return 1
    return 0

t = int(input())
for _ in range(t):
    res = chefandsum()
    if res == 1:
        print("Yes")
    elif res == 0:
        print("No")

# cook your dish here
# def chefandsum():
#     n, k = [int(x) for x in input().strip().split(" ")]
#     arr = [int(i) for i in input().split()]
#     for i in range(n):
#         for j in range(n):
#             if (i != j):
#                 if arr[i] + arr[j] == k:
#                     return 1
#     return 0

# t = int(input())
# res = [0]*t
# for i in range(t):
#     n, x = [int(x) for x in input().strip().split(" ")]
#     arr = [int(i) for i in input().split()]
#     for k in range(n):
#         for j in range(n):
#             if (k != j):
#                 if arr[k] + arr[j] == x:
#                     res[i] = 1
#                     break
#         if res[i] == 1:
#             break
# for i in range(t):
#     if res[i] == 1:
#         print("Yes")
#     elif res[i] == 0:
#         print("No")
