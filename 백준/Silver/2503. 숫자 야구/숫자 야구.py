from itertools import permutations

N = int(input())
nums = [[int(n) for n in input().split()] for _ in range(N)]

ans = 0
for perm in permutations(range(1, 10), 3):
	ok = True

	for num, s, b in nums:
		ps, pb = 0, 0

		for i in range(3):
			if str(perm[i]) == str(num)[i]:
				ps += 1
			elif str(perm[i]) in str(num):
				pb += 1

		if s != ps or b != pb:
			ok = False
			break

	if ok:
		ans += 1

print(ans)