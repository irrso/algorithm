import sys

# input
N, M = map(int, sys.stdin.readline().split())

# solve
program = dict()

for _ in range(N):
	addr, pwd = map(str, sys.stdin.readline().split())
	program[addr] = pwd

for _ in range(M):
	addr = sys.stdin.readline().rstrip()
	print(program[addr])