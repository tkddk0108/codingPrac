def solution(s):
    li = []
    for i in s:
        if i == "(":
            li.append(i)
        else:
            try: li.pop()
            except IndexError:
                return False
    if len(li) == 0:
        return True
    else:
        return False

