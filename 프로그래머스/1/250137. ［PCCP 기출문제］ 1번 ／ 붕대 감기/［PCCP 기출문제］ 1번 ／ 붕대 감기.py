from collections import deque


def solution(bandage, health, attacks):
    answer = health
    cont = 0
    
    dq = deque()
    for a, b in attacks:
        dq.append((a, b)) 
    
    for i in range(1, dq[-1][0]+1):
        if i == dq[0][0]:
            time, damage = dq.popleft()
            answer -= damage
            cont = 0
        else:
            cont += 1
            if cont == bandage[0]:
                answer += bandage[1]+bandage[2]
                answer = health if answer > health else answer
                cont = 0
            else:
                answer += bandage[1]
                answer = health if answer > health else answer
                
        if answer <= 0:
                return -1

        if not dq:
            return answer