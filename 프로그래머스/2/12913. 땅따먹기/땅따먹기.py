def solution(land):
    total = 0
    a,b,c,d = land[0][0],land[0][1],land[0][2],land[0][3] 
    for i in range(1,len(land)):
        e,f,g,h = a,b,c,d
        a,b,c,d = land[i][0],land[i][1],land[i][2],land[i][3] 
        a += max(f,g,h)
        b += max(e,g,h)
        c += max(e,f,h)
        d += max(e,f,g)


    return max(a,b,c,d)