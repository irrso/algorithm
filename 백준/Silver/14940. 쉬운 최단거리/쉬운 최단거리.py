from collections import deque
import sys

# input
n, m = map(int, sys.stdin.readline().split())
maps = [[int(i) for i in sys.stdin.readline().split()] for _ in range(n)]

# solve
dist = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
	for j in range(m):
		if maps[i][j] == 2:
			end = [i, j]
			dist[i][j] = 0
			break

dq = deque()
dq.append(end)
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

while dq:
	cy, cx = dq.popleft()

	for y, x in zip(dy, dx):
		ny, nx = cy+y, cx+x

		if (0 <= ny < n) and (0 <= nx < m) and (maps[ny][nx] == 1) and (dist[ny][nx] == -1):
			dist[ny][nx] = dist[cy][cx]+1
			dq.append([ny, nx])

for i in range(n):
	for j in range(m):
		if maps[i][j] == 0:
			print(0, end=' ')
		else:
			print(dist[i][j], end=' ')
	print()