# input
A, B = map(int, input().split())

# solve
def solve(A, B):
	for i in range(A, 0, -1):
		if A%i == 0 and B%i == 0:
			print(i)
			print(B*(A//i))
			break

A, B =  max(A, B), min(A, B)

solve(A, B)