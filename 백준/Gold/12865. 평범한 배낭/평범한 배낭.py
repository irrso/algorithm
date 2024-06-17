N, K = map(int, input().split())
things = [[int(i) for i in input().split()] for _ in range(N)]

W, V = [0], [0]
for t in things:
	W.append(t[0])
	V.append(t[1])


dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
	for k in range(1, K+1):
		dp[n][k] = dp[n-1][k]
		if W[n] <= k:
			dp[n][k] = max(dp[n-1][k], dp[n-1][k-W[n]] + V[n])

print(dp[n][k])