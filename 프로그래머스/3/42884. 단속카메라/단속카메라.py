from collections import deque

def solution(routes):
	routes = deque(sorted(routes, key=lambda x: x[1]))

	cameras=[]
	while(routes):
		car = routes.popleft()

		if not cameras:
			cameras.append(car[1])
			continue

		if car[0] <= cameras[-1] <= car[1]:
			continue

		cameras.append(car[1])

	ans = len(cameras)

	return ans