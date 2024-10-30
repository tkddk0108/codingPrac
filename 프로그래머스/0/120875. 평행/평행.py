#각 점들은 다른 하나의 점에 연결되어서 선분을 이루는 겁니다. 즉, 1번 점과 2번 점이 연결되었으면, 1번 점과 2번 점은 다른 점과 이을 수 없는 겁니다.
def solution(dots):
    #1 - 0/1 과 2/3
    a = (dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0])
    b = (dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0])
    if a == b:
        return 1
    #2 0/2과 1/3
    c = (dots[2][1]-dots[0][1]) / (dots[2][0]-dots[0][0])
    d = (dots[3][1]-dots[1][1]) / (dots[3][0]-dots[1][0])
    if c == d:
        return 1
    
    # 3 0/3과 1/2
    e = (dots[3][1]-dots[0][1]) / (dots[3][0]-dots[0][0])
    f = (dots[2][1]-dots[1][1]) / (dots[2][0]-dots[1][0])
    if e == f:
        return 1
    return 0