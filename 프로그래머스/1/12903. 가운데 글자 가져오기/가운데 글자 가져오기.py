def solution(s):
    if len(s)%2 != 0:
        return str(s[len(s)//2])
    else: 
        return str(s[len(s)//2-1]+s[len(s)//2])