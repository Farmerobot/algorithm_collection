import math

def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

n = i()
a = []
height = 0
m = 0

for x in range(n):
    a.append(i())
    height = max(height, a[x])

for x in range(n):
    for h in range(1, height + 1):
        s = 0
        for w in range(x, n):
            # exit
            if h > a[w]:
                break
            else:
                s += h
            m = max(m, s)
print(m)