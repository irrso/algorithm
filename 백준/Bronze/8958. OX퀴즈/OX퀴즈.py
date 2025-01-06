# input
N = int(input())

# solve
def count(results):
	ans, seq = 0, 1
	
	for result in results:
		if result == 'O':
			ans += seq
			seq += 1
		else:
			seq = 1

	return ans

for _ in range(N):
	results = list(map(str, input()))
	print(count(results))