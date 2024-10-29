def solution(n):
    answer = 0
    val = [0]
    #tsn = ['3','6','9']
    for i in range(n*5):
        if '3' not in str(i) and i%3 != 0:
            val.append(i)
    print(val)
    return val[n]
