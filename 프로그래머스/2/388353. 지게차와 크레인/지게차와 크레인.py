from collections import deque

def find_connected(storage, n, m):
    dq = deque()
    visited = [[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1) and storage[i][j] == -1:
                dq.append((i, j))
                visited[i][j] = True
    
    while dq:
        y, x = dq.popleft()
        
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and storage[ny][nx] == -1:
                dq.append((ny, nx))
                visited[ny][nx] = True
    
    return visited


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = n*m
    container = dict()
     
    for i in range(n):
        storage[i] = list(storage[i])
        for j in range(m):
            alpha = storage[i][j]
            if alpha not in container:
                container[storage[i][j]] = []
            container[storage[i][j]].append((i, j))
    
    for request in requests:
        if request[0] not in container:
            continue
        
        if len(request) == 1:
            out_connected = find_connected(storage, n, m)
            
            for y, x in container[request[0]]:
                if storage[y][x] == -1:
                    continue
                
                if y == 0 or y == n-1 or x == 0 or x == m-1:
                    storage[y][x] = -1
                    answer -= 1
                    continue
                
                for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m and storage[ny][nx] == -1:
                        if out_connected[ny][nx]:
                            storage[y][x] = -1
                            answer -= 1
                            break
        else:
            for y, x in container[request[0]]:
                if storage[y][x] == -1:
                    continue
                storage[y][x] = -1
                answer -= 1
                
    return answer