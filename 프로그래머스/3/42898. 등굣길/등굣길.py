def solution(m, n, puddles):
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[1][1] = 1
    
    dy, dx = [0, -1], [-1, 0]
    
    for x, y in puddles:
        dp[y][x] = -1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            
            for cy, cx in zip(dy, dx):
                ny, nx = cy+y, cx+x
                if 0 < ny <= n and 0 < nx <= m:
                    dp[y][x] += dp[ny][nx]
            
    return dp[n][m]%1000000007