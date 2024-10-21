def solution(array):
    answer = 0
    for x in array:
        x = sorted(str(x))
        for i in x:
            if i == '7': answer += 1
    return answer