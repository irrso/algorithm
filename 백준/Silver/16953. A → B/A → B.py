from collections import deque

# input
A, B = map(int, input().split())

# solve
count, is_possible = 0, False
dq = deque()
dq.append((A, count))

while dq:
	num, count = dq.popleft()

	if num == B:
		is_possible = True
		break
	if num >= B:
		continue

	dq.append((num*2, count+1))
	dq.append((int(str(num)+'1'), count+1))

print(count+1) if is_possible else print(-1)