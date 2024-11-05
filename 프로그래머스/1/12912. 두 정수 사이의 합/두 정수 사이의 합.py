def solution(a, b):
    answer = 0
    m1 = max(a,b)
    m2 = min(a,b)
    for i in range(m2, m1+1):
        answer +=  i
    return answer