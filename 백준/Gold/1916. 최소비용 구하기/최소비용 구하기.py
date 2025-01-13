import sys
import heapq

# input
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
	start, end, cost = map(int, sys.stdin.readline().split())
	adj_list[start].append((cost, end))

start, end = map(int, sys.stdin.readline().split())

# solve
def dijkstra(dist, node):
	pq = []

	heapq.heappush(pq, (0, node))
	dist[node] = 0

	while pq:
		cost, node = heapq.heappop(pq)
		if cost > dist[node]:
			continue

		for adj_cost, adj_node in adj_list[node]:
			temp_cost = cost + adj_cost
			if dist[adj_node] > temp_cost:
				heapq.heappush(pq, (temp_cost, adj_node))
				dist[adj_node] = temp_cost

dist = [int(1e12)]*(N+1)
dijkstra(dist, start)

print(dist[end])