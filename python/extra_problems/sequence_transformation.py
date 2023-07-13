import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

mat = []

N, M = intil()
S = input()
longest = S

for i in range(M):
    a, b, s = input().split(';')
    a = int(a)
    b = int(b)
    sub_S = S[0:min(a,b)]
    sub_S += s
    sub_S += S[max(a, b)+1:]
    S = sub_S
    longest = S if len(S) > len(longest) else longest
print(S)
print(longest)