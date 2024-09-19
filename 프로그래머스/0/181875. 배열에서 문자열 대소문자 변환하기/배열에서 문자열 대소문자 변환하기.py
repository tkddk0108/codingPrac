def solution(strArr):
    answer = ''
    abc = []
    for i in range(len(strArr)):
        if i%2 == 0:
            for j in strArr[i]:
                answer += j.lower()
            abc.append(answer)
            answer = ''
        else:
            for j in strArr[i]:
                answer += j.upper()
            abc.append(answer)
            answer = ''
    return abc