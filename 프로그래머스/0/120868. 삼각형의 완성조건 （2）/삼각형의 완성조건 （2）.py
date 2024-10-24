def solution(sides):
    answer = 0
    #x = max(sides) - min(sides)
    for i in range(max(sides)):
        if i + min(sides) > max(sides) and i <= max(sides):
            answer += 1
    
    for i in range(max(sides), 2*max(sides)):
        if i < sum(sides) and i >= max(sides):
            answer += 1
            
    return answer