def solution(ingredient):
    answer, i = 0, 0
    while i < len(ingredient)-3:
        if ingredient[i:i+4] == [1,2,3,1]:
            del ingredient[i:i+4]
            i = max(0, i-3)
            answer += 1
        else:
            i += 1
    return answer