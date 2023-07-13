import math
def intil():
    return [int(x) for x in input()[:-1].split(' ')]
def inti():
    return int(input())

n = inti()

def a(x, m):
    global n
    m += 1
    x -= 1
    if x == 0:
        return 1
    # elif m >= n:
        # return x
    else:
        return 1 + a(x + 1 - a(a(x, m), m), m)

print(a(n, 1))