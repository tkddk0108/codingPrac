def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def solution(balls, share):
    answer = 0
    return factorial(balls) / (factorial(balls-share) * factorial(share))
