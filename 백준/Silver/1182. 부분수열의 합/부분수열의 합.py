from itertools import combinations


# input
N, S = map(int, input().split())
nums = list(map(int, input().split()))

# solve
ans = 0
for i in range(1, N+1):
	for comb in combinations(nums, i):
		if S == sum(comb):
			ans += 1

print(ans)