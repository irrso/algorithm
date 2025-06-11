def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start = h1*3600 + m1*60 + s1
    end = h2*3600 + m2*60 + s2
    prev_hour, prev_minute, prev_second = 0, 0, 0
    
    while start <= end:
        hour = (start % 43200) / 120
        minute = (start % 3600) / 10
        second = (start % 60) * 6
        
        if second == 0:
            second = 360
            if minute < 10:
                minute += 360
            if hour < 10:
                hour += 360
            
        if prev_second < prev_hour and hour < second:
            answer += 1
        
        if prev_second < prev_minute and minute < second:
            answer += 1
        
        if second == hour or second == minute:
            answer += 1
        
        start += 1
        prev_hour, prev_minute, prev_second = hour, minute, second
    
    return answer