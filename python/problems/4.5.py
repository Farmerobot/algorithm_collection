import math
def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

t = i()

for x in range(t):
    a, m = inti()
    s = 0
    x = 0
    while s < m:
        s += a
        a *= 2
        x += 1
    print(x)
    # print(max(math.ceil(math.log2(m/a)+1), 1))