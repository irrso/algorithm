import sys

# input
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

# solve
d = dict()
for i, x in enumerate(sorted(set(X))):
	d[x] = i

for x in X:
	print(d[x], end=' ')
