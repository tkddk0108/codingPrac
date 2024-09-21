def solution(myStr):
    word = ''
    for i in myStr:
        if i not in "abc":
            word += i
        else:
            word += ' '
    answer = word.split()
    if answer ==[]:
        return ["EMPTY"]
    else:
        return answer