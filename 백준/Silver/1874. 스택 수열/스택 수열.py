from collections import deque

# input
n = int(input())
seq = list(int(input()) for _ in range(n))

# solve
def is_possible(num):
	for i in range(n):
		while(num <= seq[i]):
			dq.append(num)
			ans.append('+')
			num += 1

		if dq[-1] == seq[i]:
			dq.pop()
			ans.append('-')
		else:
			return False

	return True

num = 1
dq = deque()
ans = []

[print(ans) for ans in ans] if is_possible(num) else print('NO')