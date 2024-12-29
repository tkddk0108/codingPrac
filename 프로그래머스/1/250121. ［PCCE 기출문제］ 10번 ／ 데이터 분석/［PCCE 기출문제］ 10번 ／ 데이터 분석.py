from datetime import datetime, timedelta

def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == "date":
        val_ext = datetime.strptime(str(val_ext), "%Y%m%d")
        for i in data:
            date  = datetime.strptime(str(i[1]), "%Y%m%d")
            if val_ext > date:
                answer.append(list(i))
    elif ext == "code":
        for i in data:
            if val_ext > i[0]:
                answer.append(list(i))
    elif ext == "maximum":
        for i in data:
            if val_ext > i[2]:
                answer.append(list(i))
    elif ext == "remain":
        for i in data:
            if val_ext > i[3]:
                answer.append(list(i))
    if sort_by == "code": n = 0
    elif sort_by == "date": n = 1
    elif sort_by == "maximum": n = 2
    else: n = 3
    
    return sorted(answer, key = lambda x : x[n])