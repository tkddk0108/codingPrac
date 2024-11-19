#구현 - 왕실의 나이트
point = str(input())
alpha = ['a','b','c','d','e','f','g','h']
a = alpha.index(point[0]) + 1
b = int(point[1])
cnt = 0

if a + 2 <= 8:
    if b + 1 <= 8:
        cnt += 1
    if b - 1 >= 1:
        cnt += 1
if a - 2 >= 1:
    if b + 1 <= 8:
        cnt += 1
    if b - 1 >= 1:
        cnt += 1
if b + 2 <=8:
    if a + 1 <= 8:
        cnt += 1
    if a - 1 >= 1:
        cnt += 1
if b - 2 >= 1:
    if a + 1 <= 8:
        cnt += 1
    if a - 1 >= 1:
        cnt += 1

print(cnt)