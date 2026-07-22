def solution(x, y, n):
    answer = 0
    INF = int(1e6)
    
    dp = [INF]*(y+1)
    dp[y] = 0
    
    if x == y:
        return 0
    
    for i in range(y, x-1, -1):
        if dp[y] == INF:
            continue
            
        if i-n <= y:
            dp[i-n] = min(dp[i-n], dp[i]+1)
        
        if i%2 == 0:
            dp[i//2] = min(dp[i//2], dp[i]+1)
        
        if i%3 == 0:
            dp[i//3] = min(dp[i//3], dp[i]+1)
    
    return -1 if dp[x] == INF else dp[x]


'''
x를 y로 변환하기 위해 필요한 최소 연산 횟수
- x + n
- x * 2
- x * 3

1 <= x <= y <= 1000000
1 <= n < y
'''