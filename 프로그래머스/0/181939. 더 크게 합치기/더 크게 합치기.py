def solution(a, b):
    answer = 0
    aPb = int(str(a) + str(b))
    bPa = int(str(b) + str(a))
    if aPb > bPa:
        answer = aPb
    else:
        answer = bPa
    
    return answer