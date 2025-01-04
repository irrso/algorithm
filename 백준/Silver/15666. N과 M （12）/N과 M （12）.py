from itertools import combinations_with_replacement

# input
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# solve
cases = set()
for comb in combinations_with_replacement(sorted(nums), M):
	cases.add(comb)

for case in sorted(cases):
	[print(c, end=' ') for c in case]
	print()