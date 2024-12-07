def solution(s, skip, index):
    answer = ''
    abc = list(x for x in 'abcdefghijklmnopqrstuvwxyz')
    for i in skip:
        abc.remove(i)
    abc = abc*3
    for i in range(len(s)):
        n = abc.index(s[i])
        answer += abc[n+index]
    return answer
