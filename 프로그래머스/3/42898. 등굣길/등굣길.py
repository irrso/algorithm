def solution(m, n, puddles):
	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
	dp[1][1] = 1

	for x, y in puddles:
		dp[y][x] = -1

	dy = [0, -1]
	dx = [-1, 0]

	for y in range(1, n+1):
		for x in range(1, m+1):
			if dp[y][x] == -1:
				dp[y][x] = 0
				continue

			for i in range(2):
				ny = y + dy[i]
				nx = x + dx[i]

				if 0 < ny <= n and 0 < nx <= m:
					dp[y][x] += dp[ny][nx]


	return dp[n][m]%1000000007