def solution(l, r):
    answer = []
    num=['0','5']
    for i in range(l, r+1):
        val=''
        a = str(i)
        for j in a:
            if j in num:
                val += j 
        if val == a:
            answer.append(i)
    if answer == []:
        answer.append(-1)
        
    return answer