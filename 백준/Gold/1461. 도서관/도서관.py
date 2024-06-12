def move(arr):
	cnt = 0
	for i in range(0, len(arr) , M):
		cnt += abs(arr[i])*2

	return cnt


# input
N, M = map(int, input().split())
book = sorted(list(map(int, input().split())))

# solve
idx = N
for i in range(N):
	if book[i] > 0:
		idx = i
		break

neg = book[:idx]
pos = book[idx:]

ans = move(neg)+move(pos[::-1])

ans1 = ans-abs(neg[0]) if len(neg)!=0 else ans
ans2 = ans-pos[-1] if len(pos)!=0 else ans
ans = min(ans1, ans2)

print(ans)