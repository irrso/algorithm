def solution(people, limit):
	ans = 0
    
	people = sorted(people, reverse=True)
	p1, p2 = 0, len(people)-1
	
	while(True):
		if p1 > p2:
			break

		if p1 == p2:
			ans +=1
			break

		if people[p1]+people[p2] <= limit:
			p1 += 1; p2 -= 1
			ans += 1
		else:
			p1 += 1
			ans += 1

	return ans