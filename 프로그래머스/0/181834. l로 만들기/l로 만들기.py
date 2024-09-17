def solution(myString):
    answer = ''
    before = "abcdefghijk"
    for i in myString:
        if i in before:
            answer += 'l'
        else:
            answer += i
    return answer