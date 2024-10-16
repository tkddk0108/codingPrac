def solution(s):
    answer = 0
    val = []
    li = list(map(str, s.split()))
    for i in range(len(li)):
        if li[i] == 'Z': val.pop(-1)
        else: val.append(int(li[i]))
    return sum(val)