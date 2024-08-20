def solution(name):
	ans = 0

	move = len(name)-1
	for left, n in enumerate(name):
		ans += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)

		i = left+1
		while i < len(name) and name[i]=='A':
			i += 1

		right = len(name)-i

		print(left, right, i)

		move = min(move, right*2 + left)
		move = min(move, left*2 + right)

	ans += move
	return ans