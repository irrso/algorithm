# input
N, M = map(int, input().split())

# solve
unheard, unseen = set(), set()

for _ in range(N):
	unheard.add(input())
for _ in range(M):
	unseen.add(input())

ans = sorted(unheard&unseen)

print(len(ans))
for ans in ans:
	print(ans)