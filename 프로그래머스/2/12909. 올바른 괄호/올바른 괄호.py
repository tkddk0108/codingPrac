def solution(s):
    answer = True
    a=0
    if s[-1] == "(" or s.count("(") != s.count(")"): return False
    for i in range(len(s)-1):
        if s[i] == "(" : a += 1
        else: a -= 1
        if a < 0: return False

    return True