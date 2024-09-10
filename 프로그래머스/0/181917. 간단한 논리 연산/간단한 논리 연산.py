def solution(x1, x2, x3, x4):
    answer = True
    if x1 ==True or x2 == True: result1 = True
    else:   result1 = False
    
    if x3 ==True or x4 == True: result2 = True
    else:   result2 = False
    
    if result1 == True and result2 == True:
        answer = True
    else:
        answer = False
    return answer