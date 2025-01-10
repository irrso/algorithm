import sys
import heapq

# input
N = int(sys.stdin.readline())

# solve
heap = []
for _ in range(N):
	x = int(sys.stdin.readline())

	if x == 0:
		print(heapq.heappop(heap)) if len(heap) else print(0)
	else:
		heapq.heappush(heap, x)