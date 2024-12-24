from collections import deque
import sys

# input
N = int(sys.stdin.readline())

# solve
dq = deque()

for _ in range(N):
	ops = list(map(str, sys.stdin.readline().split()))

	if len(ops) == 2:
		dq.append(ops[1])
	elif ops[0] == 'pop':
		print(dq.popleft() if dq else -1)
	elif ops[0] == 'size':
		print(len(dq))
	elif ops[0] == 'empty':
		print(0 if dq else 1)
	elif ops[0] == 'front':
		print(dq[0] if dq else -1)
	else:
		print(dq[-1] if dq else -1)