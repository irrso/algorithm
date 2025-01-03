from itertools import combinations_with_replacement

# input
N, M = map(int, input().split())

# solve
for comb in combinations_with_replacement(range(1, N+1), M):
	[print(comb, end=' ') for comb in comb]
	print()