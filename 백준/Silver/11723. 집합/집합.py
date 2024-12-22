import sys

# input
M = int(sys.stdin.readline())

# solve
S = set()
for _ in range(M):
	ops = sys.stdin.readline().split()

	if len(ops) == 1:
		if ops[0] == 'all':
			S = set(range(1, 21))
		else:
			S = set()

	else:
		op, x = ops[0], int(ops[1])

		if op == 'add':
			S.add(x)
		elif op == 'remove':
			S.remove(x) if x in S else S
		elif op == 'check':
			print(1 if x in S else 0)
		else:
			S.remove(x) if x in S else S.add(x)