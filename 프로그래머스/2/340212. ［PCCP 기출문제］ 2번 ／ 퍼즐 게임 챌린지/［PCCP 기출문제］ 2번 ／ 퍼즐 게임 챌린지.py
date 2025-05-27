def cal_times(diffs, times, level):
    tot = 0
    for i in range(len(diffs)):
        if level >= diffs[i]:
            tot += times[i]
        else:
            tot += (times[i]+times[i-1])*(diffs[i]-level) + times[i]
    return tot
    
    
def solution(diffs, times, limit):
    start, end = 1, max(diffs)
    answer = -1
    
    while(start <= end):
        level = (start+end)//2
        tot = cal_times(diffs, times, level)
        
        if tot == limit:
            return level
        
        if tot < limit:
            end = level-1
        else:
            start = level+1
            answer = start
        
    return answer if answer != -1 else 1