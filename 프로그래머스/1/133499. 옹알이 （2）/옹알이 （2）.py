def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    no = ["ayaaya", "yeye", "woowoo", "mama"]
    for words in babbling:
        temp = words
        for i in no:
            if i in temp: 
                #print(temp)
                temp = temp.replace(i,'1')
        for i in possible:
            if i in temp: 
                #print(temp)
                temp = temp.replace(i,' ')
        if temp.strip() == '':
            #print(temp)
            answer += 1
    return answer