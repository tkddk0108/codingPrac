def solution(s):
    answer = ''
    lowerS = s.lower()
    for i in range(len(lowerS)):
        if i == 0 and lowerS[i].isalpha():
            answer += lowerS[i].upper()
        elif lowerS[i] == ' ':
            answer += ' '
        elif i >= 1 and lowerS[i-1] == ' ' and lowerS[i].isalpha():
            answer += lowerS[i].upper()
        else:
            answer += lowerS[i]
    return answer