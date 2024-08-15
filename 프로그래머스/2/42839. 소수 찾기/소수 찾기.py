from itertools import permutations

def is_prime(n):
	if n < 2:
		return False

	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			return False

	return True


def solution(numbers):
	nums = list(numbers[i] for i in range(len(numbers)))

	ans = set()
	for i in range(1, len(nums)+1):
		for perm in permutations(nums, i):
			temp = int(''.join(perm))

			if is_prime(temp):
				ans.add(temp)

	return len(ans)