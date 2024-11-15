def solution(k, score):
    answer = []
    for i in range(len(score)+1):
        if i <= k:
            ex = score[:i]
            if ex: answer.append(min(ex))
        else:
            ex = score[:i]
            ex = sorted(ex, reverse = True)
            answer.append(ex[k-1])

    return answer