#구현 - 상하좌우
'''
5
R R R U D D
'''

n = int(input())
direct = list(map(str, input().split()))
p = [1,1]

for i in direct:
    if i == 'R':
        if p[1] + 1 < n:
            p[1] += 1
    elif i == "L":
        if p[1] - 1 > 1:
            p[1] -= 1
    elif i == "D":
        if p[0] + 1 < n:
            p[0] += 1
    else:
        if p[0] > 1:
            p[0] -= 1
    print(p)
print(p[0], p[1])
