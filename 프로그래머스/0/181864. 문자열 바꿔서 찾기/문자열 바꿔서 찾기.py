def solution(myString, pat):
    answer = 0
    string = ''
    for i in range(len(myString)):
        if myString[i] == "A":
            string += "B"
        elif myString[i] == "B":
            string += "A"
    
    if pat in string: return 1
    else: return 0