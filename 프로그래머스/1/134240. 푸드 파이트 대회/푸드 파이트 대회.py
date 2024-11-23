def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] % 2 == 0:
            answer += str(i)*(food[i]//2)
        else:
            answer += str(i)*((food[i]-1)//2)
    return answer+"0"+answer[::-1]