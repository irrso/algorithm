from collections import deque
from collections import Counter

def manhattan(sec, start, end):
    path = []
    sr, sc = start
    er, ec = end
    
    while sr != er:
        sr += 1 if er > sr else -1
        sec += 1
        path.append((sec, sr, sc))
    
    while sc != ec:
        sc += 1 if ec > sc else -1
        sec += 1
        path.append((sec, sr, sc))
    
    return sec, path

def solution(points, routes):
    answer = 0
    path = []
    point = dict()
    for i, p in enumerate(points):
        point[i+1] = p
    
    for route in routes:
        sec = 0
        for i in range(len(route)-1):
            start, end = point[route[i]], point[route[i+1]]
            sec, result = manhattan(sec, start, end)
            if i == 0:
                path.append((0, start[0], start[1]))
            path += result
    
    counter = Counter(path)
    for _, count in counter.items():
        if count > 1:
            answer += 1

    return answer