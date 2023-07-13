import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

m = []

n = inti()
for y in range(n):
    m.append(intil())

maxVal = 0

for row in range(n):
    for col in range(n):
        for x in range(row, n):
            for y in range(col, n):
                s = 0
                for i in range(row, x + 1):
                    for j in range(col, y + 1):
                        s += m[i][j]
                maxVal = max(s, maxVal)
print(maxVal)