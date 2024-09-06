def solution(friends, gifts):
	n = len(friends)
	name = {f: i for i, f in enumerate(friends)}

	table = [[0 for _ in range(n)] for _ in range(n)]
	for gift in gifts:
		x, y = gift.split()
		table[name[x]][name[y]] += 1

	nxt = [0 for _ in range(n)]
	for x in range(n):
		for y in range(x+1, n):
			if table[x][y] > table[y][x]:
				nxt[x] += 1
			elif table[x][y] < table[y][x]:
				nxt[y] += 1
			else:
				gx = sum(table[x])-sum(table[i][x] for i in range(n))
				gy = sum(table[y])-sum(table[i][y] for i in range(n))
				if gx > gy:
					nxt[x] += 1
				elif gx < gy:
					nxt[y] += 1

	return max(nxt)