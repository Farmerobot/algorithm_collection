import math, copy
from collections import defaultdict
def intil():
    return [int(x) for x in input().split(' ')]
def inti():
    return int(input())

n = inti()

mat = []
for i in range(n):
    mat.append(intil())

# start, end of source, destination
def pair(s1, e1, s2, e2):
    if s1 == s2 and s1 != " " or e1 == e2 and e1 != " ":
        return 0
    _s1 = 0 if s1 == " " else s1
    _e1 = 0 if e1 == " " else e1
    _s2 = 0 if s2 == " " else s2
    _e2 = 0 if e2 == " " else e2
    o = [s1, e1, s2, e2]
    # avoid div by 0
    if mat[_s1][_e1] == 0 and mat[_s2][_e2] != 0:
        return 0
    if mat[_s2][_e2] == 0:
        div = None
        # both 0 - always proportional
        if mat[_s1][_e1] == 0:
            pass
        else:
            # never proportional
            return 0
    else:
        div = mat[_s1][_e1] / mat[_s2][_e2]
    for x in range(1, n):
        _s1 = x if s1 == " " else s1
        _e1 = x if e1 == " " else e1
        _s2 = x if s2 == " " else s2
        _e2 = x if e2 == " " else e2
        # avoid div by 0
        if mat[_s1][_e1] == 0 and mat[_s2][_e2] != 0:
            return 0
        if mat[_s2][_e2] == 0:
            # both 0 - always proportional
            if mat[_s1][_e1] == 0:
                continue
            else:
                # never proportional
                return 0
        elif div == None:
            div = mat[_s1][_e1] / mat[_s2][_e2]
        if mat[_s1][_e1] / mat[_s2][_e2] != div:
            return 0
    # print(*o)
    return 1

c = 0
for t in range(n):
    for d in range(n):
        # div_h = mat[t][0] / mat[d][0]
        # div_v = mat[0][t] / mat[0][d]
        # div_h_v = mat[t][0] / mat[0][d]
        # div_v_h = mat[0][t] / mat[d][0]
        # same_h = True if t != d else False
        # same_v = True if t != d else False
        # same_h_v = True
        # same_v_h = True
        # for x in range(1, n):
        #     if mat[t][x] / mat[d][x] != div_h:
        #         same_h = False
        #     if mat[x][t] / mat[x][d] != div_v:
        #         same_v = False
        #     if mat[t][x] / mat[x][d] != div_h_v:
        #         same_h_v = False
        #     if mat[x][t] / mat[d][x] != div_h_v:
        #         same_v_h = False
        for x in [pair(t," ",d," "), pair(t, " ", " ", d), pair(" ", t, d, " "), pair(" ", t, " ", d)]:
            c += x

print(c//2)