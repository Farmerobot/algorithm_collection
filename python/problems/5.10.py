import math
def intil():
    return [int(x) for x in input()[:-1].split(' ')]
def inti():
    return int(input())

def cipher(x):
    if x.isupper():
        return (chr((ord(x) - 65 - n) % 26 + 65))
    else:
        return (chr((ord(x) - 97 - n) % 26 + 97))

n = inti()
s = input()

answer = ""
for c in s:
    answer += cipher(c)
print(answer)