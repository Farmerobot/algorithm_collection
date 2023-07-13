from collections import defaultdict
# import math, operator
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())



N = inti()

for i in range(N):
    p1, score1, p2, score2 = sum([y for y in [i for i in [x.split(':') for x in input().split(' ')]]], [])
    score1, score2 = int(score1), int(score2)
    p1won = 1 if score1 > score2 else 0
    p2won = 1 if score2 > score1 else 0
    players[p1][0] += p1won
    players[p1][1] += score1
    players[p2][0] += p2won
    players[p2][1] += score2

# matches won - cumulative points
players = defaultdict(lambda: [0, 0])
t = [i[0] for i in sorted(players.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))]
for x in t:
    print(x)