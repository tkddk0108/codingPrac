def solution(s):
    answer = []
    for i in range(len(s)):
        value = [a for a,x in enumerate(s[:i]) if x == s[i]]
        #print(s[i], value, i)
        if value != []:
            answer.append(i-max(value))
        else:
            answer.append(-1)
        
    return answer