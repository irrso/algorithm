from collections import deque
import sys

# input
T = int(sys.stdin.readline())

# solve
for _ in range(T):
	A, B = map(int, sys.stdin.readline().split())

	dq = deque()
	visited = [False for _ in range(10001)]

	dq.append([A, ''])
	visited[A] = True

	while dq:
		num, ans = dq.popleft()

		if num == B:
			print(ans)
			break

		D = (2*num)%10000
		if not visited[D]:
			dq.append([D, ans+'D'])
			visited[D] = True

		S = (num-1)%10000
		if not visited[S]:
			dq.append([S, ans+'S'])
			visited[S] = True

		L = (num%1000)*10 + num//1000
		if not visited[L]:
			dq.append([L, ans+'L'])
			visited[L] = True

		R = num//10 + (num%10)*1000
		if not visited[R]:
			dq.append([R, ans+'R'])
			visited[R] = True
