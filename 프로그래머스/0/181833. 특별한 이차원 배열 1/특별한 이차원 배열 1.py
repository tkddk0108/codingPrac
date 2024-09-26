def solution(n):
    result = []
    answer = [0]*n
    for i in range(n):
        answer[i] = 1
        result.append(answer)
        answer = [0]*n
        
        
    return result