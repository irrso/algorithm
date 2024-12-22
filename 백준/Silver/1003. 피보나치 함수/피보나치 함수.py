# input
T = int(input())

# solve
dp = [[0 for _ in range(2)] for _ in range(41)]

dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1

for n in range(2, 41):
	dp[n][0] = dp[n-1][0] + dp[n-2][0]
	dp[n][1] = dp[n-1][1] + dp[n-2][1]

for _ in range(T):
	N = int(input())
	print(dp[N][0], dp[N][1])