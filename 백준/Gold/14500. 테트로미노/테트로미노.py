# input
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

# solve
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

ans = 0
visited = [[False]*M for _ in range(N)]

def dfs(i, j, tmp, cnt):
	global ans, visited

	if cnt == 4:
		ans = max(ans, tmp)
		return

	for y, x in zip(dy, dx):
		ny = i+y
		nx = j+x
		if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
			visited[ny][nx] = True
			dfs(ny, nx, tmp+paper[ny][nx], cnt+1)
			visited[ny][nx] = False

def other(i, j):
	global ans, visited

	dir = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (0, 1), (0, 2), (-1, 1)],
			[(0, 0), (0, 1), (-1, 1), (1, 1)], [(0, 0), (0, -1), (-1, -1), (1, -1)]]

	for d in dir:
		tmp = 0
		for dy, dx in d:
			ny = i+dy
			nx = j+dx
			if 0 <= ny < N and 0 <= nx < M:
				tmp += paper[ny][nx]
			else:
				break

		ans = max(ans, tmp)


for i in range(N):
	for j in range(M):
		visited[i][j] = True
		dfs(i, j, paper[i][j], 1)
		visited[i][j] = False
		other(i, j)

print(ans)