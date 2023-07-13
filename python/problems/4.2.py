import math

def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

n = i()

for x in range(2, math.ceil(math.sqrt(n)) + 1):
    if n % x == 0:
        print(x)
        break