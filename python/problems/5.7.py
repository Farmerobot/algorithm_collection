import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = inti()
l =[]
for i in range(n):
    l.append(input())

answer = ""
for i in range(n):
    answer += l[i][i]
print(answer)