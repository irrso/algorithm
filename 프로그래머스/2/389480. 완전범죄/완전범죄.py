def solution(info, n, m):
    INF = int(1e12)
    k = len(info)
    dp = [[[INF]*m for _ in range(n)] for _ in range(k+1)]
    dp[0][0][0] = 0
    
    for i in range(k):
        cur_a, cur_b = info[i]
        for a in range(n):
            for b in range(m):
                if dp[i][a][b] != INF:
                    nxt_a = cur_a+a
                    if nxt_a < n:
                        dp[i+1][nxt_a][b] = min(dp[i+1][nxt_a][b], nxt_a)
                
                    nxt_b = cur_b+b
                    if nxt_b < m:
                        dp[i+1][a][nxt_b] = min(dp[i+1][a][nxt_b], a)
    answer = INF
    for a in range(n):
        for b in range(m):
            if dp[k][a][b] != INF:
                answer = min(answer, a)
    
    return answer if answer != INF else -1