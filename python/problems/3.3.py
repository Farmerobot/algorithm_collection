def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

t = []
for x in range(i()):
    t.append(i())
print(len(set(t)) == 1)