from collections import deque

def solution(number, k):
	dq = deque(number[0])

	for i in range(1, len(number)):
		while k > 0 and dq and dq[-1] < number[i]:
			dq.pop()
			k -= 1

		dq.append(number[i])

		if k == 0:
			break

	ans = ''.join(dq)+number[i+1:]
	return ans[:len(number)-k]