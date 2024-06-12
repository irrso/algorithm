n = int(input())

points = []
for i in range(n):
	points.append(list(map(int, input().split(' '))))

for p in sorted(points):
	print(p[0], p[1])