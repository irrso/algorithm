from collections import deque
import sys

# input
n = int(sys.stdin.readline())
trees = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    trees[a].append([b, c])
    trees[b].append([a, c])

# solve
def dijkstra(node):
    dq = deque()
    visited = [False for _ in range(n+1)]
    dist = [0 for _  in range(n+1)]

    dq.append([node, 0])
    visited[node] = True
    dist[node] = 0

    while dq:
        cur_node, cur_dist = dq.popleft()
        for adj_node, adj_dist in trees[cur_node]:
            temp_dist = cur_dist + adj_dist
            if dist[adj_node] < temp_dist and not visited[adj_node]:
                dist[adj_node] = temp_dist
                visited[adj_node] = True
                dq.append([adj_node, temp_dist])

    return dist


dist1 = dijkstra(1)
node = dist1.index(max(dist1))
dist2 = dijkstra(node)

print(max(dist2))