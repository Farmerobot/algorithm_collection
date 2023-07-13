def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

def triangle(height):
    s = "";
    for y in range(1, height + 1):
        for x in range(y):
            s += '* '
        s += '\n'
    s = s[:-1]
    print(s)

h, n = i(), i()
for x in range(h, h + n):
    triangle(x)