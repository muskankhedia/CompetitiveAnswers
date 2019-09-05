n=int(input())
image=[]
for i in range(n):
    x=input().split(' ')
    temp=[]
    row=[]
    for j in range(3*n):
        if (j)%3==0 and j!=0:
            row.append(temp)
            temp=[]
        temp.append(int(x[j]))
        if j==(3*n-1):
            row.append(temp)
            temp=[]
    image.append(row)
c=0
raw=[]
for a in range(n):
    for b in range(n):
        if image[a][b][1] > (image[a][b][0] + image[a][b][2]):
            if c ==0:
                c=1
            raw.append([a,b])
print(raw)
# adjacent check
grp = [0]
grp = (raw[0])
print(grp)
for i in range(1, len(raw)):
    for j in range(len(grp)):
        if (abs(raw[i][0] - grp[j][0]) == 1) or (abs(raw[i][1] - grp[j][1] == 1)) or (abs(raw[i][0] - grp[j][0]) == 1 and abs(raw[i][1] - grp[j][1] == 1)):
            grp[j].append(raw[i])
            break
        length = len(grp)
        print(length)
        grp.append(0)
        grp[length].append(raw[i])
        print(grp)
lll = len(grp)
print(lll)

for ele in raw:
    for j in raw:
        if (abs(j[1] - raw[1]) == 1) or (abs(j[0] - raw[0]) == 1):
            raw.remove(raw[j])
             