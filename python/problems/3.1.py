def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

j, b = inti()
s = "NOBODY"
if j > b:
    s = "John"
elif b > j:
    s = "Betty"

print(s)