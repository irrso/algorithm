from collections import deque

# input
N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]

# solve
if not truth:
	print(M)
	exit()

dq = deque()
visited_party = [False for _ in range(M)]
visited_people = [False for _ in range(N+1)]

dq += truth[0:]

while dq:
	tp = dq.popleft()
	visited_people[tp] = True

	for i in range(M):
		if tp in party[i]:
			visited_party[i] = True
			for pp in party[i]:
				if not visited_people[pp]:
					dq.append(pp)
					visited_people[pp] = True

print(visited_party.count(False))