import itertools

t = int(input())
for _ in range(t):
    key = input()
    l = len(key)
    count = 0
    arr = range(1, l+2)
    b = list(itertools.permutations(arr))
    for ele in  range(len(b)):
        for i in range(l):
            if arr[i] == '-' and arr[i] - arr[i+1] > 0:
                count+=1
            if arr[i] == '+' and arr[i+1] - arr[i] > 0:
                count += 1
        if count == l:
            print(' '.join(map(str, b[ele]))) 
            break