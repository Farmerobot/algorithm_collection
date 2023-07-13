import math
def intil():
    return [int(x) for x in input()[:-1].split(' ')]
def inti():
    return int(input())

n = inti()
l = sorted(intil())

answer = "NO"
for i in range (n-1):
    if l[i] + 1 == l[i+1]:
        answer = "YES"
        break
print(answer)