# input
N = int(input())

# solve
def conti(nums):
	count = 0

	for num in nums:
		if num == '6':
			count += 1
			if count >= 3:
				return True
		else:
			count = 0

	return False


n, num = 0, 666

while(True):
	nums = list(str(num))

	if nums.count('6') >= 3 and conti(nums):
		n += 1
		if n == N:
			print(num)
			break

	num += 1
