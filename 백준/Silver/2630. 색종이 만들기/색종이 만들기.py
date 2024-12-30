# input
N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]

# solve
def cut(x, y, N):
	global white, blue
	psum = 0

	for i in range(y, y+N):
		for j in range(x, x+N):
			psum += square[i][j]

	if psum == 0:
		white += 1
		return
	elif psum == N**2:
		blue += 1
		return
	else:
		cut(x, y, N//2)
		cut(x+N//2, y, N//2)
		cut(x, y+N//2, N//2)
		cut(x+N//2, y+N//2, N//2)

white, blue = 0, 0
cut(0, 0, N)

print(f'{white}\n{blue}')