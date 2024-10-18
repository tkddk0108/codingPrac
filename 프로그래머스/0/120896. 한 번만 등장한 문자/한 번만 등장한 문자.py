def solution(s):
    answer = ''
    val = ''
    setS = set(s)
    for i in setS:
        if s.count(i) == 1:
            answer += i
    for i in sorted(answer):
        val += i
    return val