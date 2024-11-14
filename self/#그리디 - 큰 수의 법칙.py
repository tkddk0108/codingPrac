#그리디 - 큰 수의 법칙
N, M, K = map(int,input().split())
li = sorted(list(map(int, input().split())),reverse = True)

answer = 0
cnt = 0
for i in range(M):
    if cnt == 3:
        cnt = 0
        answer += li[1]
    else:
        cnt += 1
        answer += li[0]
    
print(answer)

