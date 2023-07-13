import math
def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

dic = {}
m = 0

for s in input():
    if not s.isalpha():
        continue
    s = s.lower()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
    m = max(m, dic[s])

sor = sorted(dic.keys())

for k in sor:
    if dic[k] == m:
        print(k)
        break