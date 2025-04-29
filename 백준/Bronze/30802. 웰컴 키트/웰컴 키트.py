# input
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

# solve
tshirts = 0
for s in size:
	d, v = divmod(s, T)
	if v != 0:
		tshirts += d+1
	else:
		tshirts += d

print(tshirts)
[print(i, end=' ' ) for i in divmod(N, P)]