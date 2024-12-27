from collections import deque
import sys

sys.setrecursionlimit(10000)

# input
T = int(input())

# solve
dy = [0, -1, 0, 1]
dx = [1, 0 , -1, 0]

def search(x, y, pos):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= ny < N and 0 <= nx < M and [nx, ny] in pos:
			pos.remove([nx, ny])
			search(nx, ny, pos)

for _ in range(T):
	M, N, K = map(int, input().split())

	pos = deque()
	for _ in range(K):
		pos.append(list(map(int, input().split())))

	ans = 0
	while pos:
		x, y = pos.popleft()
		search(x, y, pos)
		ans += 1

	print(ans)