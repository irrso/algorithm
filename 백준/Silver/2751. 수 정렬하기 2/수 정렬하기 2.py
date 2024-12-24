import sys

# input
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# solve
[print(num) for num in sorted(nums)]
