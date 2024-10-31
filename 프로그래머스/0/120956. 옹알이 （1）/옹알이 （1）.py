from itertools import permutations

def solution(babbling):
    answer = 0
    ahri = ["aya", "ye", "woo", "ma"]
    value = ''
    for i in permutations(["aya", "ye", "woo", "ma"], 2):
        value = ''
        value += i[0] + i[1]
        ahri.append(value)
    for i in permutations(["aya", "ye", "woo", "ma"], 3):
        value = ''
        value += i[0] + i[1] + i[2]
        ahri.append(value)
    for i in permutations(["aya", "ye", "woo", "ma"], 4):
        value = ''
        value += i[0] + i[1] + i[2] + i[3]
        ahri.append(value)
        
    for i in babbling:
        if i in ahri:
            answer += 1
    return answer