def solution(sizes):
    answer = 0
    b, s = [], []
    for i in sizes:
        if i[0] == i[1]:
            b.append(i[0])
            s.append(i[0])
        else:
            for x in i:
                if x == max(i): b.append(x)
                else: s.append(x)
    
    return max(b) * max(s)