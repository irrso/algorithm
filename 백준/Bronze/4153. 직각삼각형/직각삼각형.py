while(True):
	# input
	n = sorted(list(map(int, input().split())))

	if n[0]== 0 and n[1] == 0 and n[2] == 0:
		break

	# solve
	print('right') if n[2]**2 == n[0]**2 + n[1]**2 else print('wrong')
