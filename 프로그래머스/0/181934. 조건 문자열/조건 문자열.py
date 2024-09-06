# 파이썬으로 문자열로된 식 계산하기
# -> 자체 내장 함수 eval() 사용
# 엄청 간단한 함수!가 있는데 이걸 모르고 고민했다

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
