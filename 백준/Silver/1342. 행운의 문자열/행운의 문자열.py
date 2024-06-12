from itertools import permutations
import math

def is_possible(perm):
	for i in range(len(perm)-1):
		if perm[i] == perm[i+1]:
			return False

	return True


# input
S = input()

# solve
ans = 0
for perm in permutations(S, len(S)):
	if is_possible(perm):
		ans += 1

for i in range(ord('a'), ord('z')+1):
	ans //= math.factorial(S.count(chr(i)))

print(ans)