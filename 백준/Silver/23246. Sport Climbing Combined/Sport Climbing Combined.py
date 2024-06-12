n = int(input())
players = [[int(i) for i in input().split()] for _ in range(n)]


players = sorted(players, key=lambda x:(x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))
for player in players[:3]:
	print(player[0], end=' ')