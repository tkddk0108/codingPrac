def solution(a, b):
    answer = 0
    
    aPb = int(str(a) + str(b))
    Dab = 2 * a * b
    
    if Dab > aPb:
        answer = Dab
    else:
        answer = aPb
        
    return answer