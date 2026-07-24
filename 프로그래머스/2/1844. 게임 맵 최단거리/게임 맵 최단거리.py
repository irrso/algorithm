from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    
    dq = deque()
    visited = [[False]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    
    dq.append([0, 0])
    visited[0][0] = True
    dist[0][0] = 1
    
    while dq:
        cy, cx = dq.popleft()
        
        if cy == n-1 and cx == m-1:
            return dist[cy][cx]
        
        for y, x in zip(dy, dx):
            ny, nx = cy+y, cx+x
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx]:
                    dq.append([ny, nx])
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[cy][cx]+1 
    
    return -1


'''
상대 팀 진영에 최대한 빨리 도착하기 위해 지나가야 하는 칸의 개수의 최솟값
- 도착할 수 없다면 -1

최단거리: bfs

maps: n*m 크기의 개임 맵 (n, m = 1~100 자연수), 0: 벽, 1: 벽X
캐릭터: (1,1) 시작
상대방 진영: (n, m)

'''