def solution(schedules, timelogs, startday):
    answer = 0
    
    for schedule, timelog in zip(schedules, timelogs):
        if schedule%100 >= 50:
            stime = ((schedule//100)+1)*100 + ((schedule%100)+10)%60
        else:
            stime = schedule+10
        
        get = True
        for i, time in enumerate(timelog):
            if (i+startday)%7 == 6 or (i+startday)%7 == 0:
                continue    
            if time > stime:
                get = False
                break
        if get:
            answer += 1
            
    return answer