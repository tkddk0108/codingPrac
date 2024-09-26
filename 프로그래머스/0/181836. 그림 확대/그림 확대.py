def solution(picture, k):
    answer = []
    word = ''
    for i in picture:
        for j in i:
            word += j*k
        for a in range(k):
            answer.append(word)
        word = ''
    return answer