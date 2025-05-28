from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    answer = [0]*m
    
    dq = deque()
    visited = [[False]*m for _ in range(n)]
    cols = []
    
    for j in range(m):
        for i in range(n):
            cols = []
            
            if land[i][j] == 0:
                continue
            
            if visited[i][j]:
                continue
            
            dq.append((i, j))
            cols.append(j)
            visited[i][j] = True
            
            while dq:
                cy, cx = dq.popleft()
                for y, x in zip(dy, dx):
                    ny, nx = cy+y, cx+x
                    if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and land[ny][nx]:
                        cols.append(nx)
                        visited[ny][nx] = True
                        dq.append((ny, nx))
            
            area = len(cols)
            for col in list(set(cols)):
                answer[col] += area 
    
    return max(answer)