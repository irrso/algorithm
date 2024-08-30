def solution(N, number):
	dp = [[int(str(N)*i) if i else 0] for i in range(9)]

	for i in range(1, 9):
		result = set()

		if dp[i][0] == number:
			return i

		for j in range(1, i):
			for n1 in dp[j]:
				for n2 in dp[i-j]:
					dp[i].append(n1+n2)

					if n1-n2 > 0:
						dp[i].append(n1-n2)

					dp[i].append(n1*n2)

					if n1//n2 > 0:
						dp[i].append(n1//n2)

		if number in dp[i]:
			return i

	return -1