import sys

# input
N, M = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))

# solve
for n in range(1, N+1):
	nums[n] += nums[n-1]

for _ in range(M):
	i, j = map(int, sys.stdin.readline().split())
	print(nums[j]-nums[i-1])