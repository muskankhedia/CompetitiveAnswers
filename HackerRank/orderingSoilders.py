def soliders():
    t = int(input())
    while t != 0:
        t -= 1
        n = int(input())
        # for i in range(n):
        # inputArr = input().split(' ')
        # for i in range(len(inputArr)):
        #     inputArr[i] = int(inputArr[i])
        inputArr = list(map(int, input().split()))
        tmpArr = inputArr
        rank = [-1] * n
        for i in range(n):
            rank[i] = i+1
        for i in range(n):
            val = tmpArr[i]
            x = i
            for j in range(val):
                temp = tmpArr[x-1]
                tmpArr[x-1] = tmpArr[x]
                tmpArr[x] = temp

                temp = rank[x-1]
                rank[x-1] = rank[x]
                rank[x] = temp
                x -= 1
        for i in range(n):
            print(rank[i], end=" ")
        print()

soliders()
