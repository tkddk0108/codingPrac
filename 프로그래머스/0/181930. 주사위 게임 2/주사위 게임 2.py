def solution(a, b, c):
    answer = 0
    if a!=b and b!=c and c!=a:
        answer = a+b+c
    elif a==b and c!=a and c!=b:
        answer = (a+b+c) * (a*a+b*b+c*c)
    elif b==c and a!=b and a!=c:
        answer = (a+b+c) * (a*a+b*b+c*c)
    elif a==c and b!=a and b!=c:
        answer = (a+b+c) * (a*a+b*b+c*c)
    else:
        answer = (a+b+c) * (a*a+b*b+c*c) * (a*a*a+b*b*b+c*c*c)
    return answer