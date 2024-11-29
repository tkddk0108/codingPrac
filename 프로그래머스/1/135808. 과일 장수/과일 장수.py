def solution(k, m, score):
    answer, row = 0, []
    score = sorted(score, reverse=True)
    for i in range(0,len(score),m):
        row = score[i:i+m]
        if len(row) == m: 
            answer += min(row) * m * 1
    return answer