import itertools

t = int(input())
for _ in range(t):
    l, k = [int(x) for x in input().strip().split(" ")]
    a = [int(i) for i in input().split()]
    # x = eqavg(arr, k)
    b = list(itertools.permutations(a))
    for ele in  range(len(b)):
        c1, c2, sum = 0, 0, 0
        for i in range(k):
            sum = sum + b[ele][i]
        m = sum / k
        for i in range(len(b[ele]) - k + 1):
            j = i
            sum = 0
            while j < (i + k):
                sum = sum + b[ele][j]
                j += 1
            c1+=1
            if (sum/k) == m:
                c2+=1
        if c1 == c2:
            print ("YES")
            print(' '.join(map(str, b[ele]))) 
            break
    if c1 != c2:
        print("NO")
