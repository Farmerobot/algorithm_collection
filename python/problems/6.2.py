def inti():
    return int(input())

def su(n, s, i):
    i -= 1
    if(i < 0):
        return s
    else:
        return su(n, s + int(n[i]), i)

n = input().split(' ')
l = len(n)

print(su(n, 0, l))