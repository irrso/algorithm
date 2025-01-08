# input
A, B = map(int, input().split())

# solve
def gcd(A, B):
	for i in range(A, 0, -1):
		if A%i == 0 and B%i == 0:
			print(i)
			break

def lcm(A, B):
	i = 1
	while(True):
		if (A*i)%B == 0:
			print(A*i)
			break
		i += 1

A, B =  max(A, B), min(A, B)

gcd(A, B)
lcm(A, B)