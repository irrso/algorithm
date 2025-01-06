# input
sound = list(map(int, input().split()))

# solve
asc = list(range(1, 9))
des = list(range(8, 0, -1))

if sound == asc:
	print('ascending')
elif sound == des:
	print('descending')
else:
	print('mixed')