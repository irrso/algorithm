from collections import deque

def solution(priorities, location):
    dq = deque((p, i) for i, p in enumerate(priorities))
    
    maximum = max(dq)[0]
    ans = 1
    while(dq):
        prior, index = dq.popleft()

        if prior < maximum:
            dq.append((prior, index))
            continue

        if index == location:
            return ans

        maximum = max(dq)[0]
        ans += 1