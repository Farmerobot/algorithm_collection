import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

def palindrome(s):
    return s == s[::-1]

s = input().lower()
answer = "NO"
for c1 in range(len(s)):
    s_copy = s
    s1 = s[:c1] + s[c1 + 1:]
    # print(s1)
    if palindrome(s1):
        answer = "YES"
        break
    for c2 in range(len(s)):
        s2 = s1[:c2] + s1[c2 + 1:]
        # print(s2)
        if palindrome(s2):
            answer = "YES"
            break
if palindrome(s):
    answer = "YES"
print(answer)