def start():
    n = int(input())
    x = (2*n)+1

    arr = [[j for j in input().strip().split(" ")] for i in range(x)] 

    for i in range(x):
        arr2 = arr
        y = x
        for j in range(y):
            if i != j:
                for j in 


def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))

start()