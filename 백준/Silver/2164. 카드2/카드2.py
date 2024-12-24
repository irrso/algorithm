from collections import deque

# input
N = int(input())
dq = deque(range(1, N+1))

# solve
while True:
	card = dq.popleft()

	if not dq:
		print(card)
		break

	dq.append(dq.popleft())