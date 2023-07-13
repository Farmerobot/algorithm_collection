def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

a = i()
t = inti()

s = 0
for x in t:
    s += 1/x

print(1/s)