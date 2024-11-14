def solution(a, b):
    answer = ''
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = 0
    for i in range(a-1):
        cnt += mon[i]
    cnt += b
    print(sum(mon))
    return week[cnt%7]

