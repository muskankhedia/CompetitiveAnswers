t = int(input())

for _ in range(t):
    rows, cols = [int(x) for x in input().strip().split(" ")]
    
    max = rows * cols
    res = [max]
    for k in range(1, max):
        arr = [0 for i in range(max)]  
        i = 0 
        while i < max:
            arr[i] = 1
            i += (k + 1)
        arr1 = [0 for i in range(max)]  

        i = 0
        for p in range(cols):
            for q in range(rows):
                xxx = (q*cols) + p
                arr1[i] = arr[xxx]
                i += 1
        
        i = 0 
        while i < max:
            arr1[i] = 1
            i += (k + 1)

        count = 0
        for i in range(max):
            if arr1[i] == 1:
                count += 1
        res.append(count)
    print(' '.join(map(str, res)))  
        
        


    