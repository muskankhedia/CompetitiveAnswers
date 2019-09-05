from collections import Counter
import math

n, t = [int(x) for x in input().strip().split(" ")]

pos = [int(i) for i in input().split()]

x=int(input())
for _ in range(x):
    s, e = [int(x) for x in input().strip().split(" ")]
    tt=[]
    for i in range(s-1, e):
        tt.append(pos[i])
    cc=Counter(tt)
    print("ccc:::::", cc)
    ans=list(cc.values())
    mm=0
    poss=-1
    import operator
    mm=max(ans)
    poss=ans.index(mm)
    if mm > math.floor(len(tt)/2):
        rr=list(cc.keys())
        print(rr[poss])
    else:
        print("Champion")