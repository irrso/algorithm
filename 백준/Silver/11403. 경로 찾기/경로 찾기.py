from queue import PriorityQueue

# input
N = int(input())
adj_matrix = [list(map(int, input().split()))for _ in range(N)]

# solve
def dijkstra(n):
	pq = PriorityQueue()
	visited = [0 for _ in range(N)]

	pq.put(n)

	while not pq.empty():
		cur_node = pq.get()
		for adj_node, possible in enumerate(adj_matrix[cur_node]):
			if not visited[adj_node] and possible:
				pq.put(adj_node)
				visited[adj_node] = 1

	return visited

for n in range(N):
	ans = dijkstra(n)
	for ans in ans:
		print(ans, end=' ')
	print()