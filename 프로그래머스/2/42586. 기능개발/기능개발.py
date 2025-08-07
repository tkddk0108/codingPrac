def solution(progresses, speeds):
    answer = []
    days = []
    count = 0
    for i in range(len(progresses)):
        work=progresses[i]
        day = 0 
        while work < 100:
            work += speeds[i]
            day += 1
        days.append(day)
    print(days)
    standard = days[0]
    for i in range(len(days)):
        count += 1
       # print(count)
        try:
            if standard < days[i+1]:
                answer.append(count)
                count = 0
                standard = days[i+1]
            else:
                if standard < days[i]:
                    standard = days[i]
                #print(standard, count)
        except IndexError:
                answer.append(count)
                
    return answer