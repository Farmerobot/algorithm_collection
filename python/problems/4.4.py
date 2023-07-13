import math

def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

def matrix(h):
    t = []
    for x in range(h):
        t.append(inti())
    return t

w1, h1 = inti()
m1 = matrix(h1)
w2, h2 = inti()
m2 = matrix(h2)

target = []

for col in range(h1):
    t = []
    for row in range(w2):
        s = 0
        for y in range(w1):
            s += m1[col][y] * m2[y][row]
        t.append(s)
    target.append(t)

for x in range(h1):
    for y in range(w2):
        print(target[x][y], end=" ")
    print("")