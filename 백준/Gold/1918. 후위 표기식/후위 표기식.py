from collections import deque

# input
exp = deque(input())

# solve
dq = deque()

for e in exp:
	if e.isalpha():
		print(e, end='')
		continue

	if e == '(':
		dq.append(e)
	elif e == '*' or e == '/':
		while dq and (dq[-1] == '*' or dq[-1] == '/'):
			print(dq.pop(), end='')
		dq.append(e)
	elif e == '+' or e == '-':
		while dq and dq[-1] != '(':
			print(dq.pop(), end='')
		dq.append(e)
	elif e == ')':
		while dq and dq[-1] != '(':
			print(dq.pop(), end='')
		dq.pop()

while dq:
	print(dq.pop(), end='')