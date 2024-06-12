n = int(input())
a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]

s = 0
for a in sorted(a):
	s += a*max(b)
	b.remove(max(b))

print(s)