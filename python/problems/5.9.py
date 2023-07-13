import math
def intil():
    return [int(x) for x in input()[:-1].split(' ')]
def inti():
    return int(input())

n = inti()
num = inti()
for i in range(n - 1):
    if inti() != num:
        print("False")
        break
else:
    print("True")