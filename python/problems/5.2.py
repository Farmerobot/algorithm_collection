import math
def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

t = sorted(inti())
l = len(t)

if l == 1 or l == 2:
    print(True)
else:
    diff = t[1] - t[0]
    for x in range(2, l):
        if t[x] - t[x-1] != diff:
            print("False")
            break
    else:
        print("True")