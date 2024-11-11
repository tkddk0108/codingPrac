def solution(t, p):
    value = []
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            value.append(int(t[i:i+len(p)]))
    print(value)
    return len(value)