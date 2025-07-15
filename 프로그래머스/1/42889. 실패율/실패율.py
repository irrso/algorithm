def solution(N, stages):
    answer = []
    cur = [0]*(N+2)
    fail = []
    
    for stage in stages:
        cur[stage] += 1
    
    for i in range(1, N+1):
        if cur[i] == 0:
            fail.append([i, 0])
        else:
            fail.append([i, cur[i]/sum(cur[i:])])
    
    for i, j in sorted(fail, key=lambda x: (-x[1], x[0])):
        answer.append(i)
            
    return answer