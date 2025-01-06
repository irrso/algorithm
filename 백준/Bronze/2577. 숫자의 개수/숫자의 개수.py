# input
A = int(input())
B = int(input())
C = int(input())

# solve
num = str(A*B*C)
[print(num.count(str(i))) for i in range(10)]