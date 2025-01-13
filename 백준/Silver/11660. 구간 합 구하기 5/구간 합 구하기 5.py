import sys

# input
N, M = map(int, sys.stdin.readline().split())
nums = [[0]*(N+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# solve
for i in range(1, N+1):
    for j in range(2, N+1):
        nums[i][j] += nums[i][j-1]

for i in range(1, N+1):
    for j in range(2, N+1):
        nums[j][i] += nums[j-1][i]

for _ in range(M):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

  ans = nums[x2][y2] - nums[x2][y1-1] - nums[x1-1][y2] + nums[x1-1][y1-1]
  print(ans)