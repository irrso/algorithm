from queue import PriorityQueue

def search(node, n):
	global dist

	INF = int(1e12)

	pq = PriorityQueue()
	pq.put([0, node])

	dist = [INF]*n
	dist[node] = 0
	visited = [False]*n

	while not pq.empty():
		cur_dist, cur_node = pq.get()

		if visited[cur_node]:
			continue

		visited[cur_node] = True

		for adj_node, adj_dist in adj_list[cur_node]:
			if not visited[adj_node] and adj_dist < dist[adj_node]:
				dist[adj_node] = adj_dist
				pq.put([adj_dist, adj_node])


def solution(n, costs):
	global adj_list

	adj_list = [[] for _ in range(n)]
	for n1, n2, cost in costs:
		adj_list[n1].append([n2, cost])
		adj_list[n2].append([n1, cost])

	search(0, n)
	ans = sum(dist)

	return ans