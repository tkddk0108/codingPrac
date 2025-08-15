def solution(priorities, location):
    answer, n = 0, 0
    wait = {}
    for i in priorities:
        wait[n] = i
        n += 1
        
    n, count = 0, 0
    
    while wait:
        m = max(wait.values())
        key, value= (next(iter(wait.items())))
        print(m)
        # 아직 차례 아님
        if value < m:
            wait.pop(key)
            wait[key] = value
        # 빠질 차례임
        else:
            answer += 1
            if key == location:
                return answer
            wait.pop(key)

    return answer