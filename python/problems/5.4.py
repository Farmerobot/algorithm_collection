import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = inti()
l = intil()

print(' '.join(str(i) for i in sorted(l)))