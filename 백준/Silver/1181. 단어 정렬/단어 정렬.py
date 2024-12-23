# input
N = int(input())
words = list(set(input() for _ in range(N)))

# solve
words = sorted(words, key=lambda x: (len(x), x))
[print(ans) for ans in words]