# input
N, K = map(int, input().split())

# solve
n1, n2 = 1, 1

for i in range(K, 0, -1):
	n1 *= N
	n2 *= i
	N -= 1

print(n1//n2)