def solution(name, yearning, photo):
    answer = []
    value = {}
    for i in range(len(name)):
        value[name[i]] = yearning[i]
    for i in photo:
        total = 0
        for j in i:
            if value.get(j) != None: total += value.get(j)
        answer.append(total)
    return answer