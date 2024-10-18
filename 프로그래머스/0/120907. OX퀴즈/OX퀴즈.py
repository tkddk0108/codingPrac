def solution(quiz):
    answer = []
    li = []
    for i in quiz:
        li = i.split()
        if li[1] == "-":
            if int(li[0]) - int(li[2]) == int(li[4]):
                answer.append("O")
            else: answer.append("X")
        elif li[1] == "+":
            if int(li[0]) + int(li[2]) == int(li[4]):
                answer.append("O")
            else: answer.append("X")
        li = []
    return answer