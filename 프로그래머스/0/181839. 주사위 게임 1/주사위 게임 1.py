def solution(a, b):
    if a%2==1 and b%2==1:
        return a*a+b*b
    elif a%2==1 or b%2==1:
        return 2*(a+b)
    elif a%2==0 and b%2==0:
        return abs(a-b)
  