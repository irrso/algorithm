# input
N, r, c = map(int, input().split())

# solve
def find(i, j, n):
	global cnt

	if i+n <= r or j+n <= c:
		cnt += (n**2)
		return

	if n > 2:
		n //= 2
		find(i, j, n)
		find(i, j+n, n)
		find(i+n, j, n)
		find(i+n, j+n, n)
	else:
		if i == r and j == c:
			print(cnt)
		elif i == r and j+1 == c:
			print(cnt+1)
		elif i+1 == r and j == c:
			print(cnt+2)
		else:
			print(cnt+3)
		exit()

cnt = 0
find(0, 0, 2**N)