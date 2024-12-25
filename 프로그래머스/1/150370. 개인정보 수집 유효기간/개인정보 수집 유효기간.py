def solution(today, terms, privacies):
    answer = []
    term  = {}
    a,b,c = map(int, today.split("."))
    now = a*12*28 + b*28 + c
    for i in terms:
        a,b  = map(str, i.split())
        term[a] = int(b)

    for i in range(len(privacies)):
        a,b = map(str, privacies[i].split())
        c,d,e = map(int, a.split("."))
        due = c*12*28 + d*28 + e + term[b]*28
        if now >= due: 
            answer.append(i+1)
    return answer