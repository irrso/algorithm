from queue import PriorityQueue
import sys

# input
T = int(sys.stdin.readline())

# solve
for _ in range(T):
	k = int(sys.stdin.readline())
	max_pq = PriorityQueue()
	min_pq = PriorityQueue()
	cnt = {}

	for _ in range(k):
		op, n = map(str, sys.stdin.readline().split())
		n = int(n)

		if op == 'I':
			max_pq.put(-n)
			min_pq.put(n)
			if n not in cnt:
				cnt[n] = 0
			cnt[n] += 1
		elif n == 1:
			while not max_pq.empty():
				x = -max_pq.get()
				if cnt[x] != 0:
					cnt[x] -= 1
					break
		elif n == -1:
			while not min_pq.empty():
				x = min_pq.get()
				if cnt[x] != 0:
					cnt[x] -= 1
					break

	max_val, min_val = int(1e12), int(-1e12)
	while not max_pq.empty():
		x = -max_pq.get()
		if cnt[x] != 0:
			max_val = x
			break

	while not min_pq.empty():
		x = min_pq.get()
		if cnt[x] != 0:
			min_val = x
			break

	if max_val == int(1e12):
		print('EMPTY')
	else:
		print(max_val, min_val)
