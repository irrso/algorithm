from queue import PriorityQueue
import sys

# input
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
	a, b, cost = map(int, sys.stdin.readline().split())
	adj_list[a].append((b, cost))

# solve
INF = int(1e12)

def dijkstra(node):
	pq = PriorityQueue()
	cost = [INF for _ in range(n+1)]

	pq.put([node, 0])
	cost[node] = 0

	while not pq.empty():
		cur_node, cur_cost = pq.get()

		if cur_cost > cost[cur_node]:
			continue

		for adj_node, adj_cost in adj_list[cur_node]:
			temp_cost = cur_cost + adj_cost
			if temp_cost < cost[adj_node]:
				pq.put([adj_node, temp_cost])
				cost[adj_node] = temp_cost

	return cost

for node in range(1, n+1):
	cost = dijkstra(node)
	for c in cost[1:]:
		if c == INF:
			c = 0
		print(c, end=' ')
	print()