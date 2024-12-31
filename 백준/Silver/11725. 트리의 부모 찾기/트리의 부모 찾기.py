import sys

sys.setrecursionlimit(10**9)

# input
N = int(input())

# solve
def search(parent, n):
	global adj_list, visited, ans

	visited[n] = True
	ans[n] = parent

	for adj_node in adj_list[n]:
		if not visited[adj_node]:
			search(n, adj_node)

adj_list = [[] for _ in range(N+1)]
visited = [False]*(N+1)
ans = dict()

for _ in range(N-1):
	i, j  = map(int, input().split())
	adj_list[i].append(j)
	adj_list[j].append(i)

search(0, 1)

[print(ans[i]) for i in range(2, N+1)]