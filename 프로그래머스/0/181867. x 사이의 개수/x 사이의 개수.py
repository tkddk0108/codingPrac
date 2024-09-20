def solution(myString):
    answer = []
    long = myString.split("x")
    for i in long:
        answer.append(len(i))
    return answer