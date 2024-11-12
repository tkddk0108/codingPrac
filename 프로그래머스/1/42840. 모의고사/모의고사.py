def solution(answers):
    answer = []
    cnt1, cnt2, cnt3 = 0,0,0
    math1 = [1,2,3,4,5] * (len(answers)//5+1)
    math2 = [2,1,2,3,2,4,2,5] * (len(answers)//8+1)
    math3 = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10+1)
    
    #print(len(math1),len(math2), len(math3))
          
    for i in range(len(answers)):
        if answers[i] == math1[i]: 
            cnt1 += 1
        if answers[i] == math2[i]: 
            cnt2 += 1
        if answers[i] == math3[i]: 
            cnt3 += 1
        #print(answers[i])
    maxi = [cnt1, cnt2, cnt3]
    
    for i in range(len(maxi)):
        if maxi[i] == max(maxi):
            answer.append(i+1)
    return answer