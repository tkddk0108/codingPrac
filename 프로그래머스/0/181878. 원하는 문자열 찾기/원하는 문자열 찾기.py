def solution(myString, pat):
    answer = ''
    pat2 = ''
    for i in myString:
        if i.islower() == True:
            answer += i.upper()
        else:
            answer += i
    
    for i in pat:
        if i.islower() == True:
            pat2 += i.upper()
        else:
            pat2 += i        

    if pat2 in answer: return 1
    else: return 0
