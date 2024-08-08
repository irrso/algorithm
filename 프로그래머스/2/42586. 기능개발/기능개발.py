import math
from collections import deque

def solution(progresses, speeds):
    ans = []

    date = deque()
    for p, s in zip(progresses, speeds):
        date.append(math.ceil((100-p)/s))

    while(date):
        cnt = 1
        temp = date.popleft()

        while(date and temp >= date[0]):
            cnt += 1
            date.popleft()

        ans.append(cnt)

    return ans