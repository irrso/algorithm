# input
K, N = map(int, input().split())
lines = list(int(input()) for _ in range(K))

# solve
def is_possible(n):
	cnt = 0
	for line in lines:
		cnt += (line//n)

	return True if cnt >= N else False

ans = 0
left, right = 0, max(lines)

mid = right

while left <= right:
	if is_possible(mid):
		left = mid + 1
		ans = mid
	else:
		right = mid - 1

	mid = (left+right)//2

print(ans)