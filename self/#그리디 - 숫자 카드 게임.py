#그리디 - 숫자 카드 게임.py
n, m = map(int, input().split()) #n줄 m행
li = []
for _ in range(n):
    row = list(map(int, input().split()))
    li.append(row)

cnt = 0
value = []
answer = []

for i in range(n):
    for j in range(m):
        value.append(li[i][j])
    answer.append(min(value))
    #print(value)
    value = []

print(max(answer))