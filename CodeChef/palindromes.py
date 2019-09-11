from itertools import combinations
t=int(input())

def palin(str):
    l = len(str)
    p = l-1
    index = 0
    # if len(str) == 1:
    #     return True
    if len(str) == 2:
        if str[0] == str[1]:
            return True
    while index < p:
        if str[index] == str[p]:
            index = index + 1
            p = p-1
            if index == p or index + 1 == p:
                return True
        else:
            return False

for _ in range(t):
    s=input()
    xx=input().split(' ')
    print(xx)
    Q=int(xx[0])
    l=int(xx[1])
    r=int(xx[2])
    x=int(xx[3])
    y=int(xx[4])
    M=int(xx[5])
    n=len(s)
    ans=0
    c=0
    for _ in range(Q):
        c = 0
        l=1 + (l+ans)%n
        r=1+(r+ans)%n
        lissst=[]
        if l > r:
            l, r = r, l
        x=1+(x+ans)%M
        y=1+(y+ans)%n
        if x > y:
            x, y = y, x
        print(str(l) + " " + str(r) + " "+ str(x)+ ' '+str(y))
        for i in range(x-1, y):
            for j in range(l-1, r+2):
                xxxx=s[j:j+i]
                print("xxx is " + xxxx)
                if palin(xxxx):
                        print("palin is "+xxxx)
                        c=c+1
        print("thii " + str(c))
        ans= ans + c 
    print(ans)

