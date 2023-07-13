def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

def ar(t):
    s = 0
    for x in range(len(t)):
        s += t[x-1][0] * t[x][1] - t[x-1][1] * t[x][0]
    return abs(s)/2

l = [a, b, c] = inti(), inti(), inti()

print ("True" if ar(l) == 0 else "False")