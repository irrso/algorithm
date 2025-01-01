import sys

# input
A, B, C = map(int, sys.stdin.readline().split())

# solve
def multiply(A, B):
	if B == 1:
		return A%C
	else:
		b = multiply(A, B//2)
		if B%2 == 0:
			return (b*b)%C
		else:
			return(b*b*A)%C

print(multiply(A, B))