def divide(num):
    for i in range(2, num):
        if num % i == 0 : return i
    return num

def solution(n):
    answer = []
    while n != 1:
        num = divide(n)
        answer.append(num)
        n //= num 
    
    return sorted(list(set(answer)))