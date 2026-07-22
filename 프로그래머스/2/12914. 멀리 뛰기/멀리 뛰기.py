def solution(n):
    dp = [0]*(n+1)
    dp[1] = 1
    
    for i in range(2, n+1):
        if i > 2:
            dp[i] = dp[i-1]+dp[i-2]
            continue
        dp[i] = 2
        
    return dp[n]%1234567


'''
끝에 도달하는 방법의 개수%1234567
- 한번에 1칸 또는 2칸 뜀

1 = 1
2 = 2
3 = 3
4 = 5 
5 = 8
6 = 13

n: 1이상 2000 이하 정수
'''