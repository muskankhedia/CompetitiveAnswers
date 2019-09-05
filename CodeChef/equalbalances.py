t = int(input())
def equalbal (arr, avg, cost):
    i = 0
    max = [1000]
    arr1 = []
    arr2 = []
    while i < len(arr):
        if arr[i] < avg:
            ar = list()
            ar.append(arr[i])
            ar.append(i+1)
            arr1.append(ar)
        if arr[i] > avg:
            ar = list()
            ar.append(arr[i])
            ar.append(i+1)
            arr2.append(ar)
    
    for j in range(arr1):
        for k in range(arr2):
            t = (arr2[k][0] - avg)*abs((arr2[k][1] - arr1[j][1]))
            if t < max[0]:
                max[0] = t
                max[1] = j
                max[2] = k
    cost = cost + max[0]
    arr1[max[1]][0] += (arr2[max[2]]-avg)
    arr2[max[2]][0] += (arr2[max[2]]-avg)
    arr[arr1[max[1]][1]] = arr1[max[1]][0]
    arr[arr2[max[2]][1]] = arr2[max[2]][0]
    result = all(elem == arr[0] for elem in arr)
    if result:
        return (cost)
    else:
        equalbal(arr, avg, cost)

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    avg = sum(arr)/len(arr)
    cost = 0
    if len(arr) > 0 :
        result = all(elem == arr[0] for elem in arr)
    if result:
        print(cost)
    else:
        cost = equalbal (arr, avg, cost)



