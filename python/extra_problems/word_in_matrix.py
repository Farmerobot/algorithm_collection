import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

mat = []

n, m = intil()
S = input()
for y in range(n):
    mat.append((input()))

maxVal = 0

answer = "NO"
def test(s):
    global answer, S
    if (s == S or s == S[::-1]):
        answer = "YES"
        return True
    else:
        return False

for row in range(n):
    for col in range(m):
        s = ""
        for x in range(row, n):
            s += mat[x][col]
            if test(s):
                break
        s = ""
        for y in range(col, m):
            s += mat[row][y]
            if test(s):
                break
print(answer)