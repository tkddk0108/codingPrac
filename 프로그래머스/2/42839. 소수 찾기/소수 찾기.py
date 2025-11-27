from itertools import permutations
def check(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
    
def solution(numbers):
    lst = list(numbers) 
    setnum=set()
    
    for r in range(1, len(lst)+1):
        for p in permutations(lst, r):
            setnum.add(int("".join(p)))
    
    answer = 0
    for i in setnum:
        if check(i): answer += 1
    
    return answer