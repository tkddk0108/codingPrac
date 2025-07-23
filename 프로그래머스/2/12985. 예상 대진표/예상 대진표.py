def solution(n,a,b):
    answer = 0
    for i in range(n//2):
        if a%2 == 0: a = a//2
        else: a = a//2+1
        
        if b%2 ==0: b= b//2
        else: b= b//2 + 1
        answer+= 1
        if a ==b : return answer
