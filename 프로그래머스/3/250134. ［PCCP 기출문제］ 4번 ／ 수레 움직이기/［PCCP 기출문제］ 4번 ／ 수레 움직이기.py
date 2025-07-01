from queue import deque
import copy

def solution(maze):
    n, m = len(maze), len(maze[0])
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                r_start = [i, j, 0]
            elif maze[i][j] == 2:
                b_start = [i, j, 0]
    
    r_visited = [[False]*m for _ in range(n)]
    b_visited = [[False]*m for _ in range(n)]
    dq = deque()
    
    dq.append([r_start, b_start, r_visited, b_visited])
    r_visited[r_start[0]][r_start[1]] = True
    b_visited[b_start[0]][b_start[1]] = True
    
    while dq:
        r_pos, b_pos, r_vst, b_vst = dq.popleft()
        ry, rx, rcost = r_pos
        by, bx, bcost = b_pos
        
        if maze[ry][rx] == 3 and maze[by][bx] == 4:
            return max(rcost, bcost)
        
        if maze[ry][rx] == 3:
            for y, x in zip(dy, dx):
                ny, nx = y+by, x+bx
                if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] != 5 and not b_vst[ny][nx]:
                    if (ry, rx) != (ny, nx):
                        b_vst[ny][nx] = True
                        dq.append([[ry, rx, rcost], [ny, nx, bcost+1], r_vst, b_vst])
                        continue
        
        if maze[by][bx] == 4:
            for y, x in zip(dy, dx):
                ny, nx = y+ry, x+rx
                if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] != 5 and not r_vst[ny][nx]:
                    if (by, bx) != (ny, nx):
                        r_vst[ny][nx] = True
                        dq.append([[ny, nx, rcost+1], [by, bx, bcost], r_vst, b_vst])
                        continue
        
        for y1, x1 in zip(dy, dx):
            nry, nrx = y1+ry, x1+rx
            rc_vst, bc_vst = copy.deepcopy(r_vst), copy.deepcopy(b_vst)
            if not (0 <= nry < n and 0 <= nrx < m and maze[nry][nrx] != 5 and not rc_vst[nry][nrx]):
                continue
            
            for y2, x2 in zip(dy, dx):
                nby, nbx = y2+by, x2+bx
                if 0 <= nby < n and 0 <= nbx < m and maze[nby][nbx] != 5 and not bc_vst[nby][nbx]:
                    if (nry, nrx) != (nby, nbx) and (nry, nrx, nby, nbx) != (by, bx, ry, rx):
                        rc_vst[nry][nrx] = True
                        bc_vst[nby][nbx] = True
                        dq.append([[nry, nrx, rcost+1], [nby, nbx, bcost+1], rc_vst, bc_vst])

    return 0