def solution(s):
    answer = ''
    for i in range((len(s))):
        if i == 0:
            if s[i].isalpha(): answer += s[i].upper()
            else: answer += s[i]
        else:
            if s[i-1] == " ":
                if s[i].isalpha(): answer += s[i].upper()
                else: answer += s[i]
            else:
                if s[i].isalpha(): answer += s[i].lower()
                else: answer += s[i]
    return answer