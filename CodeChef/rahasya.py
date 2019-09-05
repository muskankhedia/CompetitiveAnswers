t = int(input())
output = ''
n = 10000
sum = 0
for i in range(n):
    if i != 0:
        output = output + str(i)


for _ in range(t):
    x = int(input())
    v = output[x-1]
    sum = sum + int(v)

print(sum)
