n = int(input())

change = 1000 - n
cnt = 0

for yen in [500, 100, 50, 10, 5, 1]:
	cnt += change // yen
	change %= yen

print(cnt)