def solution(x):
    num = [int(n) for n in str(x)]
    if x % sum(num) == 0: return True
    return False
