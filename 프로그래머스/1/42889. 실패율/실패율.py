def solution(N, stages):
    answer = []
    total = len(stages)
    fail = dict()
    for i in range(1, N+1):
        if stages.count(i) != 0:
            fail[i] = stages.count(i) / total
        else:
            fail[i] = 0
        total -= stages.count(i)
            
    return sorted(fail, key = lambda x: fail[x], reverse = True)