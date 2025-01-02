from itertools import permutations

# input
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# solve
for perm in permutations(sorted(nums), M):
	[print(perm, end=' ') for perm in perm]
	print()