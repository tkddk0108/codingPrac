def solution(schedules, timelogs, startday):
    answer = 0
    maxi = []
    for sched in schedules:
        hour, minute = divmod(sched, 100)  # 시, 분 분리
        total_minutes = hour * 60 + minute  # 분 단위로 변환
        total_minutes += 10                 # 10분 더하기

        # 다시 시:분으로 환산
        new_hour, new_minute = divmod(total_minutes, 60)
        # 정수로 다시 표현 (예: 10시 5분 → 1005)
        maxi.append(new_hour * 100 + new_minute)

    print(maxi)
        
    for i in range(len(maxi)):
        last = int(maxi[i])
        check = []
        #print(answer)
        for j in range(len(timelogs[0])):
            start = (startday + j)%7
            if start==6 or start==0:
                continue
                
            if timelogs[i][j] > last:
                check.append(-1)
                break
            #print(timelogs[i][j], start, check)
        if len(check) < 1:
            answer += 1


    return answer