import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = inti()
mat = []
x, y = intil()

for i in range(n):
    mat.append(intil())

target_x = 101
# loop until both at target
while True:
    # find smallest value in row
    new_y = mat[x].index(min(mat[x]))

    # found new column
    if (new_y != y):
        y = new_y
        continue

    # find smallest value in column
    val_x = float('inf')
    index_x = -1
    for i in range(n):
        if val_x > mat[i][y]:
            val_x = mat[i][y]
            index_x = i
    target_x = index_x

    # update and exit if no more moves
    if (x == target_x):
        x = target_x
        break
    # update pos and loop again
    x= target_x

print(x, y)