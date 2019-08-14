def mat(n):
    size = len(n)
    for i in range(size):
        for j in range(size):
            n[i][j] = 0
    
    for k in range(1, size+1):
        