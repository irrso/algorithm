from collections import deque

def search(node, k):
	visited = [False]*(N+1)

	dq = deque()
	dq.append(node)
	visited[node] = True

	cnt = 0

	while(dq):
		node = dq.popleft()

		for adj_node, usado in adj_list[node]:
			if visited[adj_node] or usado < k:
				continue
			dq.append((adj_node))
			visited[adj_node] = True
			cnt += 1

	print(cnt)


# input
N, Q = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
	p, q, r = map(int, input().split())
	adj_list[p].append((q, r))
	adj_list[q].append((p, r))

# solve
for _ in range(Q):
	k, v = map(int, input().split())
	search(v, k)