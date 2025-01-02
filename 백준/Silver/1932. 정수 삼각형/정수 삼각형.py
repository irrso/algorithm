# input
n = int(input())
tri = []
for _ in range(n):
	tri += list(map(int, input().split()))

# solve
dp = [0]*(sum(range(1, n+1)))
dp[0] = tri[0]

idx = 0
for i in range(1, n):
	prev = idx
	idx += i
	dp[idx] = dp[prev] + tri[idx]

idx = 0
for i in range(2, n+1):
	prev = idx
	idx += i
	dp[idx] = dp[prev] + tri[idx]

idx = 4
for i in range(3, n+1):
	for j in range(i-2):
		dp[idx+j] = max(dp[idx+j-i], dp[idx+j-i+1]) + tri[idx+j]

	idx += i

print(max(dp[-n:]))