import math
def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

def ar(t):
    s = 0
    for x in range(len(t)):
        s += t[x-1][0] * t[x][1] - t[x-1][1] * t[x][0]
    return abs(s)/2

max_a = 0
min_a = math.inf
points = []
n = i()

for x in range(n):
    points.append(inti())
for a in points:
    for b in points:
        for c in points:
            area = ar([a, b, c])
            if area == 0:
                continue
            min_a = min(min_a, area)
            max_a = max(max_a, area)
print(min_a, max_a)
