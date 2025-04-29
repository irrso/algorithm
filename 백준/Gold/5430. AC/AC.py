from collections import deque

# input
T = int(input())

# solve
for _ in range(T):
	p = list(input())
	n = int(input())

	dq = deque()
	for num in map(str, input().split(',')):
		if n == 0:
			break

		if num[0] == '[':
			num = num[1:]

		if num[-1] == ']':
			num = num[:-1]
		dq.append(num)

	error, reverse = False, False
	for func in p:
		if func == 'R':
			reverse = not reverse
		elif func == 'D' and dq:
			dq.pop() if reverse else dq.popleft()
		else:
			print('error')
			error = True
			break

	if error:
		continue

	ans = ['[']
	while dq:
		ans.append(dq.pop()) if reverse else ans.append(dq.popleft())
		ans.append(',')

	if ans != list('['):
		ans = ans[:-1]
	ans.append(']')
	
	[print(ans, end='') for ans in ans]
	print()