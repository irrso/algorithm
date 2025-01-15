from collections import deque

# input
K = int(input())

# solve
dq = deque()
for _ in range(K):
	n = int(input())

	if n == 0:
		dq.pop()
		continue

	dq.append(n)

print(sum(dq))


