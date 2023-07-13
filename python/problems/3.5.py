import math

def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

def p(k):
    if (k in [2, 3, 5, 7]):
        return True
    if (k == 0 or k == 1 or k % 2 == 0 or k % 3 == 0):
        return False
    for x in range(6, max(math.ceil(math.sqrt(k)), 7), 6):
        if (k % (x+1) == 0 or k % (x-1) == 0):
            return False
    return True

n = i()

for x in range(n):
    if (p(x)):
        print(x)