def solution(s):
    answer, i= 0, 1
    c1, c2 = 1, 0
    t = s[0]
    while i < len(s):
        if s[i] != t:
            c2 += 1
        else:
            c1 += 1
        i += 1
        
        if c1 == c2:
            #print(c1, c2)
            answer += 1
            c1, c2 = 0, 0
            if i < len(s): t = s[i]
    if c1 >= 1: answer += 1
    return answer