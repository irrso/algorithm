from collections import deque

# input
N = int(input())
grid = [[i for i in input()] for _ in range(N)]

# solve
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

dq = deque()
visited = [[False]*N for _ in range(N)]
ans1 = 0

for y in range(N):
	for x in range(N):
		if visited[y][x]:
			continue

		dq.append((y, x))
		visited[y][x] = True
		ans1 += 1

		while dq:
			cy, cx = dq.popleft()

			for iy, ix in zip(dy, dx):
				ny = cy+iy
				nx = cx+ix

				if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and grid[cy][cx] == grid[ny][nx]:
					dq.append((ny, nx))
					visited[ny][nx] = True

dq = deque()
visited = [[False]*N for _ in range(N)]
ans2 = 0

for y in range(N):
	for x in range(N):
		if visited[y][x]:
			continue

		dq.append((y, x))
		visited[y][x] = True
		ans2 += 1

		while dq:
			cy, cx = dq.popleft()

			for iy, ix in zip(dy, dx):
				ny = cy+iy
				nx = cx+ix

				if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
					if (grid[cy][cx] == 'B' and grid[cy][cx] == grid[ny][nx]) or (grid[cy][cx] != 'B' and grid[ny][nx] != 'B'):
						dq.append((ny, nx))
						visited[ny][nx] = True

print(ans1, ans2)