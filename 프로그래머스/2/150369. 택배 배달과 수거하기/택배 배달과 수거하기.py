from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    n = len(deliveries)
    delivery, pickup = deque(), deque()
    
    for i in range(n):
        if deliveries[i] != 0:
            for _ in range(deliveries[i]):
                delivery.append(i+1)
            
        if pickups[i] != 0:
            for _ in range(pickups[i]):
                pickup.append(i+1)
    
    truck, d_dist, is_first = 0, [], True
    while delivery:
        dist = delivery.pop()
        
        if truck+1 <= cap:
            truck += 1
            if is_first:
                d_dist.append(2*dist)
                is_first = False
        else:
            delivery.append(dist)
            truck, is_first = 0, True
    
    truck, p_dist, is_first = 0, [], True
    while pickup:
        dist = pickup.pop()
        
        if truck+1 <= cap:
            truck += 1
            if is_first:
                p_dist.append(2*dist)
                is_first = False
        else:
            pickup.append(dist)
            truck, is_first = 0, True

    d, p = len(d_dist), len(p_dist)
    for i in range(max(d, p)):
        if i >= d:
            answer += p_dist[i]
        elif i >= p:
            answer += d_dist[i]
        else:
            answer += max(d_dist[i], p_dist[i])
    
    return answer