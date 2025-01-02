from itertools import permutations

# input
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# solve
cases = set()
for perm in permutations(nums, M):
	cases.add(perm)

for case in sorted(cases):
	[print(c, end=' ') for c in case]
	print()