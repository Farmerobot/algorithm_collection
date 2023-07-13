import math, copy
from collections import defaultdict
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

m, n = intil()

mat = []
for i in range(m):
    mat.append(intil())

k = inti()

for i in range(k):
    s = input()
    temp_mat = [[0] * m for i in range(n)]
    if len(s) == 1:
        for x in range(m):
            for y in range(n):
                temp_mat[y][x] = mat[x][y]
        m, n = n, m
    else:
        temp_mat = copy.deepcopy(mat)
        num = int(s[3:])
        if s[1] == 'R':
            for x in range(n):
                temp_mat[num][x] = mat[num][::-1][x]
        else:
            for x in range(m):
                temp_mat[x][num] = mat[::-1][x][num]
    mat = temp_mat

for x in range(m):
    s = ""
    for y in range(n):
        s += str(mat[x][y]) + " "
    print(s)