import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

mat = []

n, m = intil()
for y in range(n):
    mat.append((intil()))

maxVal = 0

for i in range(m):
    s = 0
    for j in range(min(n, m - i)):
        s += mat[j][i + j]
    maxVal = max(maxVal, s)
    # print("r: " + str(s))
    s = 0
    for j in range(min(n, i + 1)):
        s += mat[j][i - j]
    # print("l: " + str(s))
    maxVal = max(maxVal, s)

for i in range(n):
    s = 0
    for j in range(min(m, n - i)):
        s += mat[i + j][j]
    maxVal = max(maxVal, s)
    # print("r: " + str(s))
    s = 0
    for j in range(min(m, i + 1)):
        s += mat[i - j][j]
    # print("l: " + str(s))
    maxVal = max(maxVal, s)

print(maxVal)