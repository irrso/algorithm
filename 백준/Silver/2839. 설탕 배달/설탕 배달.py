# input
N = int(input())

# solve
INF = int(1e12)
dp = [0 for _ in range(N+1)]

for n in range(N+1):
	if n == 0 or n == 1 or n == 2 or n == 4:
		dp[n] = INF
		continue

	if n == 3 or n == 5:
		dp[n] = 1
		continue

	if dp[n-3] == INF and dp[n-5] == INF:
		dp[n] = INF
		continue

	dp[n] = min(dp[n-3], dp[n-5])+1

print(dp[N] if dp[N] != INF else -1)