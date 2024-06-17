a = " " + input()
b = " " + input()

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

for n in range(1, len(a)):
	for m in range(1, len(b)):
		if a[n] == b[m]:
			dp[n][m] = dp[n-1][m-1] + 1
		else:
			dp[n][m] = max(dp[n][m-1], dp[n-1][m])

print(dp[n][m])