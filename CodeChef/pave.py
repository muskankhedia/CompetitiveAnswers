import math

a, b = [int(x) for x in input().strip().split(" ")]
mul = a * b
num = math.ceil(mul/2)
print(num)