# input
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# solve
ans = 0
for a in sorted(A, reverse=True):
	div, mod = divmod(K, a)
	ans += div
	K = mod

print(ans)