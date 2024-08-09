from collections import deque

def solution(priorities, location):
    dq = deque((p, i) for i, p in enumerate(priorities))

    ans = 1
    while(True):
        prior, index = dq.popleft()

        if dq and prior < max(dq)[0]:
            dq.append((prior, index))
            continue

        if index == location:
            return ans

        ans += 1