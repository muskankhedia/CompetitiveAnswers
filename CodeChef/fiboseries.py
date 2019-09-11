t=int(input())
def deller(a):
    b=[]
    for i in range(len(a)):
        if i % 2 == 1:
            b.append(a[i])
    return b

while t!=0:
    t=t-1
    n=int(input())
    # generating
    fib = []
    fib.append(0)
    fib.append(1)
    arr=[0,1]

    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
        arr.append(fib[i]%10)
    # deleting
    while (len(arr) != 1):
        arr = deller(arr)
    print(arr[0])
