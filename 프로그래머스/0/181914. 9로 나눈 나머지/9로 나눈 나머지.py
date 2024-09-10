def solution(number):
    answer = 0
    strnum=str(number)
    total = 0
    for i in range(len(strnum)):
        total += int(strnum[i])
    answer = total % 9
    return answer