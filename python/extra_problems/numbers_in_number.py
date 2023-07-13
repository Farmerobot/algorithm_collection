import math
from collections import defaultdict
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = input()
nlen = len(n)

for i in range(nlen):
    nums = defaultdict(lambda: 0)
    for x in range(nlen - i):
        nums[n[x:x+i + 1]] += 1
    print(sorted(nums.items(), key = lambda x: (-x[1], x[0]))[0][0])