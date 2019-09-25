t = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def calculateValue(arr):
    sum = 0
    for x in arr:
        for each in range(len(x)):
            sum = sum + (each + alpha.index(x[each]))
    sum = sum * len(arr)
    return sum

for _ in range(t):
    sum = 0
    arr = [i for i in input().split()]
    sum = calculateValue(arr)
    print(sum)
    