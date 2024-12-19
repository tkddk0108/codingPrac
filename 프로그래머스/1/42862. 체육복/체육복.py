def solution(n, lost, reserve):
    answer = 0
    dic = [1] * n
    lost = sorted(lost)
    
    for i in range(1, n+1):
        if i in lost:
            dic[i-1] -= 1
        if i in reserve:
            dic[i-1] += 1

    for j in range(n):
        if j > 0 and dic[j] == 0and dic[j-1] == 2:
            dic[j] += 1
            dic[j-1] -= 1
        if j < n-1 and dic[j] == 0 and dic[j+1] == 2:
            dic[j] += 1
            dic [j+1] -= 1
    
    for i in range(len(dic)):
        if dic[i] >= 1:
            answer += 1
    return answer