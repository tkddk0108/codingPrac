def solution(ineq, eq, n, m):
    answer = 0
    if eq == '!': operator = ineq
    else: operator = ineq + eq
        
    sol = str(n) + operator + str(m)
    a= bool(eval(sol))
    
    if a == True:
        answer = 1
    else:
        answer = 0
    return answer