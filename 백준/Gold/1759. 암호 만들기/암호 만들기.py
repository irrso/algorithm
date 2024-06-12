from itertools import combinations

def password(word):
	vow = 0
	for w in word:
		if w in ['a', 'e', 'i', 'o', 'u']:
			vow += 1
	con = L- vow
	
	return (vow >= 1 and con >= 2)


# input
L, C = map(int, input().split())
alpha = sorted(input().split())

# solve
for word in combinations(alpha, L):
	if password(word):
		print(''.join(word))