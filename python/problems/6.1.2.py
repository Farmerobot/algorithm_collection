import sys
from functools import lru_cache
def intil():
    return [int(x) for x in input()[:-1].split(' ')]
def inti():
    return int(input())

n = inti()

sys.setrecursionlimit(1500)
@lru_cache(maxsize=None)
def a(x):
    global n
    x -= 1
    if x == 0:
        return 1
    else:
        return 1 + a(x + 1 - a(a(x)))

print(a(n))