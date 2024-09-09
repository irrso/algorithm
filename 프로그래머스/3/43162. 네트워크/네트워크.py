def dfs(node, visited, n, computers):
	visited[node] = True

	for i in range(n):
		if computers[node][i] and not visited[i]:
			dfs(i, visited, n, computers)


def solution(n, computers):
	ans = 0
	visited = [False]*n

	for i in range(n):
		if not visited[i]:
			dfs(i, visited, n, computers)
			ans += 1

	return ans