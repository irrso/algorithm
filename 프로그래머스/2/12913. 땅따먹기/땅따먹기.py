def solution(land):
    N = len(land)
    dp = land

    for n in range(1, N):
        for m in range(4):
            dp[n][m] += max(dp[n-1][m-3], dp[n-1][m-2], dp[n-1][m-1])
    
    return max(dp[-1])


'''
마지막 행까지 내려왔을 때 얻을 수 있는 점수의 최댓값
- 각 행의 4칸 중 한칸만 밟으면서 내려옴
- 같은 열을 연속해서 밟을 수 없음

dp[n][m]: m칸을 밟고 n행까지 내려왔을때의 점수
dp[n][m] = max(dp[n-1][m제외])

행의 개수 N: 100,000 이하 자연수
열의 개수: 4
점수: 100 이하의 자연수
'''