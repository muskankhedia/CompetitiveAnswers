import math

t = int(input())

for _ in range(t):
    a1, a2, a3, c1, c2, c3 = [int(x) for x in input().strip().split(" ")]
    if (a1 > a2 and c1 > c2) or (a1 == a2 and c1 == c2) or (a1 < a2 and c1 < c2):
        if (a1 > a3 and c1 > c3) or (a1 == a3 and c1 == c3) or (a1 < a3 and c1 < c3):
            if (a2 > a3 and c2 > c3) or (a2 == a3 and c2 == c3) or (a2 < a3 and c2 < c3):
                print ("FAIR")
            else:
                print ("NOT FAIR")
        else:
            print ("NOT FAIR")
    else:
        print ("NOT FAIR")