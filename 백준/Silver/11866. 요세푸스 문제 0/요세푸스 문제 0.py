from collections import deque

# input
N, K = map(int, input().split())

# solve
dq = deque(range(1, N+1))
ans = []

while dq:
	for _ in range(K-1):
		dq.append(dq.popleft())

	ans.append(str(dq.popleft()))

print('<'+', '.join(ans)+'>')