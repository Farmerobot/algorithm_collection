import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

s, p = input(), input()
# ls = len(s)
# lp = len(p)

if p in s:
    print("YES")
else:
    print("NO")

# answer = "NO"
# for i in range(ls - lp + 1):
#     if s[i:i+lp] == p:
#         answer = "YES"
#         break

# print(answer)