def solution(myString, pat):
    answer = 0
    for i in range(len(myString)+1):
        if pat in myString[i:i+len(pat)]:
            answer += 1
            print(pat, myString[i:])
    return answer