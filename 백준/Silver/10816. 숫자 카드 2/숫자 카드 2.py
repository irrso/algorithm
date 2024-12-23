# input
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# solve
ans = dict()
for card in cards:
	ans[card] = ans[card]+1 if card in ans else 1

[print(ans[num] if num in ans else 0, end=' ') for num in nums]
