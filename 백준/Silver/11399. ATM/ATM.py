# input
N = int(input())
P = list(map(int, input().split()))

# solve
ans = 0
P = sorted(P, reverse=True)

for (i, p) in enumerate(P):
	ans += (i+1)*p

print(ans)