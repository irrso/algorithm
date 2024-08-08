from collections import deque

def solution(arr):
	ans = []
	dq = deque()

	for i in range(len(arr)):
		if i == 0:
			dq.append(arr[i])
			continue

		if dq[-1] != arr[i]:
			dq.append(arr[i])

	while(dq):
		ans.append(dq.popleft())

	return ans