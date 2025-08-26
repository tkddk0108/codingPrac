def solution(N, stages):
    answer = []
    total = {}
    for i in range(1,N+1):
        if i in stages:
            rate = stages.count(i)/len(stages)
            total[i] = rate
            stages = [x for x in stages if x != i]
        else:
            total[i] = 0
    s_total = sorted(total.items(), key = lambda x:x[1], reverse = True)
    return [k for k,v in s_total]