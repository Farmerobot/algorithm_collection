import math
def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

s = ""
for c in input():
    if c.lower() not in ('a', 'e', 'i', 'o', 'u', 'y'):
        s += c
print(s)