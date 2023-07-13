def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

a = inti()
n = len(a)
m = 0

for x in range(n):
    s = 0
    for y in range(x, n):
        s += a[y]
        m = max(m, s)

print(m)