def solution(s):
    answer = True
    a = list()
    for i in s:
        if i == "(":
            a.append(i)
        else:
            try:
                a.pop()
            except IndexError:
                return False
            
    if len(a) == 0: return True
    else: return False
