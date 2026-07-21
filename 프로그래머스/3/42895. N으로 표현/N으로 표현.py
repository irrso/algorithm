from collections import deque
from itertools import product

def solution(N, number):
    dp = [{int(str(N)*i) if i else 0} for i in range(9)]

    for n in range(1, 9):
        for i in range(1, n//2+1):
            for n1, n2 in product(dp[i], dp[n-i]):
                dp[n].add(n1+n2)
                dp[n].add(n1*n2)
                dp[n].add(max(n1//n2, n2//n1))
                if n1-n2 != 0 or n2-n1 != 0:
                    dp[n].add(max(n1-n2, n2-n1))

        if number in dp[n]:
            return n
    
    return -1