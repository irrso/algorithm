from collections import deque

# input
N, M = map(int, input().split())
ladder = dict()
for _ in range(N):
	x, y = map(int, input().split())
	ladder[x] = y

snake = dict()
for _ in range(M):
	u, v = map(int, input().split())
	snake[u] = v

# solve
dq = deque()
visited = [False for _ in range(101)]

dq.append((1, 0))
visited[1] = True

while dq:
	node, cnt = dq.popleft()

	if node == 100:
		print(cnt)
		exit()

	for i in range(1, 7):
		nxt_node = node+i

		if nxt_node > 100:
			continue

		if nxt_node in ladder:
			nxt_node = ladder[nxt_node]
		elif nxt_node in snake:
			nxt_node = snake[nxt_node]

		if not visited[nxt_node]:
			visited[nxt_node] = True
			dq.append((nxt_node, cnt+1))
