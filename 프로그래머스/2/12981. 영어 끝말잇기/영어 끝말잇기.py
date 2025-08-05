def solution(n, words):
    answer = []
    past = []
    a,b,i = 0,0,-1
    for word in words:
        i += 1
        a = i % n + 1   # 사람 번호 (1부터 시작)
        b = i // n + 1  # 그 사람이 몇 번째로 말했는지
        #print(a,b)
        #print(past)
        if len(past) > 0:
            last = past[-1]
            #print(last)
            if word in past or last[-1] != word[0]:
                    return [a,b]
        past.append(word)

    return [0,0]