# input
N = int(input())
A = [0] + list(map(int, input().split()))

# solve
dp = [0 for _ in range(N+1)]

for n in range(1, N+1):
	for i in range(n-1, 0, -1):
		if A[n] > A[i]:
			dp[n] = max(dp[n], dp[i])
	dp[n] += 1

print(max(dp))