from itertools import combinations

def check_list(arg):
    for i in arg:
        if arg.count(i) > 1:
            return True
            
n, k = [int(x) for x in input().strip().split(" ")]

arr = [int(i) for i in input().split()]
count=1
count += n
ll = []
for i in range(2, k+1):
    comb=list(combinations(arr, i))
    print(comb)
    for j in range(len(comb)):
        temp = comb[j]
        found =False
        found = check_list(temp)
        # for k in range(len(temp)-1):
        #     temp2 = temp[k]
        #     if temp2 in temp[k+1:]:
        #         found=True
        #         break
        if found:
            break
        if not found:
            count+=1

print(count)

