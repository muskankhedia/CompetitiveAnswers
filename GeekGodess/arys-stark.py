import itertools

# x = itertools.combinations(range(2), 4)
t = int(input())
for _ in range(t):
    suma = 0
    sums = 0
    count = 0
    found = False
    r, p = [int(x) for x in input().strip().split(" ")]
    x =  list(itertools.combinations_with_replacement(range(2), r))
    print(x)
    for i in x:
        y = list(dict.fromkeys(list (itertools.permutations(i))))
        # print(y)
        for c in y:
            suma = 0
            sums = 0
            found = False
            for j in range(len(c)):
                if c[j] == 0:
                    suma += 1
                else:
                    sums += 1
                if suma >= p * sums:
                    found = True
                else:
                    found = False
                    break
            if found:
                count += 1
    print(count)