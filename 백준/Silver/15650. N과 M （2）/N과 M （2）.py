from itertools import combinations

# input
N, M = map(int, input().split())

# solve
for comb in combinations(range(1, N+1), M):
	[print(comb, end=' ') for comb in comb]
	print()