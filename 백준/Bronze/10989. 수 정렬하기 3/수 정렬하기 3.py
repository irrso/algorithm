import sys

# input
N = int(sys.stdin.readline())

# solve
nums = [0]*10001

for _ in range(N):
	nums[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
	if nums[i] != 0:
		for _ in range(nums[i]):
			print(i)