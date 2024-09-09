from collections import deque

def solution(maps):
	n, m = len(maps), len(maps[0])

	dy = [0, 1, 0, -1]
	dx = [1, 0, -1, 0]

	dq = deque()
	visited = [[False for _ in range(m)] for _ in range(n)]

	dq.append((1, 0, 0))
	visited[0][0] = True

	while(dq):
		dist, y, x = dq.popleft()

		if y == n-1 and x == m-1:
			return dist

		for i in range(4):
			cy = y + dy[i]
			cx = x + dx[i]
			if 0 <= cy < n and 0 <= cx < m and not visited[cy][cx] and maps[cy][cx]==1:
				dq.append((dist+1, cy, cx))
				visited[cy][cx] = True

	return -1