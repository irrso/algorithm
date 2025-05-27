from queue import PriorityQueue
import sys

# input
N = int(sys.stdin.readline())

# solve
pos_pq = PriorityQueue()
neg_pq = PriorityQueue()

for _ in range(N):
	x = int(sys.stdin.readline())

	if x:
		if x > 0:
			pos_pq.put(x)
		else:
			neg_pq.put(-x)
	else:
		if pos_pq.empty() and neg_pq.empty():
			print(0)
			continue
		elif pos_pq.empty():
			neg = -neg_pq.get()
			print(neg)
			continue
		elif neg_pq.empty():
			pos = pos_pq.get()
			print(pos)
			continue

		pos, neg = pos_pq.get(), -neg_pq.get()
		if pos >= -neg:
			print(neg)
			pos_pq.put(pos)
		else:
			print(pos)
			neg_pq.put(-neg)
