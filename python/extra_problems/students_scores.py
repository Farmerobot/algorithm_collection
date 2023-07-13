import math
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = inti()
student_dict = {}
test_dict = {}

for i in range(n):
    s = input().split(' ')
    student = s.pop(0)
    grade_sum = 0
    grade_count = 0
    for i, [key, val] in enumerate([x.split(':') for x in s]):
        test_dict[key] = [test_dict.get(key, [0, 0])[0] + float(val), test_dict.get(key, [0, 0])[1] + 1]
        grade_sum += float(val)
        grade_count = i + 1
    student_dict[student] = grade_sum / grade_count
for x in sorted(student_dict.items()):
    print(f"{x[0]} {x[1]}")
for x in sorted(test_dict.items()):
    print(f"{x[0]} {x[1][0]/x[1][1]}")
