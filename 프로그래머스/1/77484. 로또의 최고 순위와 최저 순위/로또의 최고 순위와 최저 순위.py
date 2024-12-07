def solution(lottos, win_nums):
    answer = [0] * 2
    cnt = 0
    rank = [0,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            cnt += 1
    if cnt <= 1: answer[1] = 6
    else: answer[1] = rank.index(cnt)
    
    cnt += lottos.count(0)
    if cnt <= 1: answer[0] = 6
    else: answer[0] = rank.index(cnt)
    return answer