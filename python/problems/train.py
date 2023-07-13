def inti():
    return int(input())

n = inti()
# Name, Delay
trains = {}

for x in range(n):
    line = input().split()
    trains[line[1] + line[2]] = [line[0], 0]

m = inti()

for x in range(m):
    line = input().split()
    trains[line[3] + line[5]][1] += int(line[10])

for t in sorted(trains.items(), key = lambda x: (-x[1][1], x[1][0])):
    print(t[1])