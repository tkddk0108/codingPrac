def solution(s):
    answer = ''
    li = sorted(list(map(str, s)),reverse = True)
    for x in li:
        answer += x
    return answer