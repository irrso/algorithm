from collections import deque

# input
M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# solve
dz = (0, 0, -1, 1, 0, 0)
dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, 0, 0, -1, 1)

idx = []
for y in range(H):
	for z in range(N):
		for x in range(M):
			if boxes[y][z][x] == 1:
				idx.append((y, z, x))

dq = deque()
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
ans = 0

for i in idx:
	dq.append((ans, i))

while dq:
	ans, (y, z, x) = dq.popleft()

	for ny, nz, nx in zip(dy, dz, dx):
		cy = y+ny
		cz = z+nz
		cx = x+nx

		if 0 <= cy < H and 0 <= cz < N and 0 <= cx < M and boxes[cy][cz][cx] == 0:
			dq.append((ans+1, (cy, cz, cx)))
			boxes[cy][cz][cx] = 1

for y in range(H):
	for z in range(N):
		for x in range(M):
			if boxes[y][z][x] == 0:
				print(-1)
				exit()
print(ans)