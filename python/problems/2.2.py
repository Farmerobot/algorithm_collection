def inti():
    return [int(x) for x in input().split(' ')]

[a, b] = inti()
s = 0

for x in range (a, b + 1):
    s += x**2

print(s)