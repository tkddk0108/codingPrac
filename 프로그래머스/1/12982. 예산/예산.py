def solution(d, budget):
    answer = 0
    cnt = 0
    for i in sorted(d):
        if answer+i <= budget:
            answer += i
            cnt += 1
    
    return cnt