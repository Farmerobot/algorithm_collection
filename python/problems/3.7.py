def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

n, x, y = inti()

s = 0

for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            for d in range(n + 1):
                if x * (a * a - c * c) + y * (b * b - d * d) == 0:
                    s += 1
print(s)