from queue import PriorityQueue

def solution(scovile, k):
	pq = PriorityQueue()
	[pq.put(s) for s in scovile]
	
	ans = 0
	while True:
		if pq.queue[0] >= k:
			break

		if len(pq.queue) <= 1:
			ans = -1
			break

		new_scovile = pq.get() + pq.get()*2
		pq.put(new_scovile)
		ans += 1

	return ans