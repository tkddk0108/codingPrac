def solution(x, n):
    answer = []
    end = x*n+1
    if x <= 0: end = x*n-1
    if x == 0: return [0]*n
    for i in range(x, end, x):
        answer.append(i)
    return answer