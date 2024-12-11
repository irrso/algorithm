from collections import deque


def is_possible():
	for box in boxes:
		if 0 in box:
			return False
	return True
		
M, N = map(int, input().split())
boxes = [[i for i in map(int, input().split())] for _ in range(N)]

tomato = deque()
for n in range(N):
	for m in range(M):
		if boxes[n][m] == 1: tomato.append((n, m))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

ans = 0
while(True):
	temp = deque()
	while(tomato):
		n, m = tomato.popleft()
		for i in range(4):
			ny = n+dy[i]
			nx = m+dx[i]
			if 0 <= ny < N and 0 <= nx < M and boxes[ny][nx]==0:
				boxes[ny][nx]=1
				temp.append((ny, nx))
	tomato=temp
	if not tomato:
		print(ans) if is_possible() else print(-1)
		break

	ans += 1
