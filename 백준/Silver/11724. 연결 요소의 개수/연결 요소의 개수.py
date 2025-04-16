from collections import deque
import sys
sys.setrecursionlimit(10**6)

# input
N, M = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
	u, v = map(int, sys.stdin.readline().split())
	adj_list[u].append(v)
	adj_list[v].append(u)

# solve
dq = deque()
visited = [False for _ in range(N+1)]

def graph(n):
	if visited[n]:
		return False

	dq.append(n)
	visited[n] = True

	while dq:
		cur_node = dq.pop()
		for adj_node in adj_list[cur_node]:
			graph(adj_node)

	return True

ans = 0
for n in range(1, N+1):
	if graph(n):
		ans += 1

print(ans)