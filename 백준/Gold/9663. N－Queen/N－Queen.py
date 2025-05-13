# input
N = int(input())

# solve
def solution(n):
	ans = 0

	def backtrack(row, cols, diag1, diag2):
		nonlocal ans

		if row == n:
			ans += 1
			return

		for col in range(n):
			if col in cols or (row+col) in diag1 or (row-col) in diag2:
				continue

			backtrack(row+1, cols|{col}, diag1|{row+col}, diag2|{row-col})

	backtrack(0, set(), set(), set())

	return ans

print(solution(N))