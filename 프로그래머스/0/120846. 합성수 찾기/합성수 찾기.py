def solution(n):
    answer = []
    cnt = 0
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0 : 
                cnt += 1
        if cnt >= 3: 
            answer.append(i)
        cnt = 0
            
        
    print(answer)
    return len(answer)