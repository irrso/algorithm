# input
N = int(input())
infos = [list(map(str, input().split())) for _ in range(N)]

# solve
infos = sorted(infos, key=lambda x: int(x[0]))
[print(age, name) for (age, name) in infos]