def inti():
    return [int(x) for x in input().split(' ')]
def i():
    return int(input())

t = i()
for x in range(t):
    n, m = inti()
    if n > m:
        s = f"{n}  is greater than  {m}"
    elif n < m:
        s = f"{n}  is smaller than  {m}"
    else:
        s = f"n is equal m:  {n}"
    print(s)