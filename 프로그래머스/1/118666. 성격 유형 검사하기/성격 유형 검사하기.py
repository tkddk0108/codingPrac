def solution(survey, choices):
    answer = ''
    R, T, C, F, J, M, A, N = 0, 0, 0, 0, 0, 0, 0, 0
    choice = [3,2,1,0,1,2,3]
    for i in range(len(survey)): 
        #print(survey[i], choices[i], choices[i]-1, choice[choices[i]-1])
        if survey[i] == "RT":
            if choices[i] <= 3: R += choice[choices[i]-1]
            else: T += choice[choices[i]-1]
        elif survey[i] == "TR":
            if choices[i] <= 3: T += choice[choices[i]-1]
            else: R += choice[choices[i]-1]
        elif survey[i] == "FC":
            if choices[i] <= 3: F += choice[choices[i]-1]
            else: C += choice[choices[i]-1]
        elif survey[i] == "CF":
            if choices[i] <= 3: C += choice[choices[i]-1]
            else: F += choice[choices[i]-1]
        elif survey[i] == "MJ":
            if choices[i] <= 3: M += choice[choices[i]-1]
            else: J += choice[choices[i]-1]
        elif survey[i] == "JM":
            if choices[i] <= 3: J += choice[choices[i]-1]
            else: M += choice[choices[i]-1]
        elif survey[i] == "AN":
            if choices[i] <= 3: A += choice[choices[i]-1]
            else: N += choice[choices[i]-1]
        elif survey[i] == "NA":
            if choices[i] <= 3: N += choice[choices[i]-1]
            else: A += choice[choices[i]-1]
    
    
    if R >= T: answer += "R"
    else: answer += "T"
    if C >= F: answer += "C"
    else: answer += "F"
    if J >= M: answer += "J"
    else: answer += "M"
    if A >= N: answer += "A"
    else: answer += "N"
    
    return answer