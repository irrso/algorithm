def solution(money):
    house = len(money)
    money = [0]+money
    
    dp1 = [0]*(house+1)
    dp1[1] = money[1]
    for n in range(2, house):
        dp1[n] = max(dp1[n-1], dp1[n-2]+money[n])
    
    dp2 = [0]*(house+1)
    for n in range(2, house+1):
        dp2[n] = max(dp2[n-1], dp2[n-2]+money[n])
    
    return max(dp1[-2], dp2[-1])


'''
도둑이 훔칠 수 있는 돈의 최댓값
- 인접한 두 집은 털 수 없음

dp[n] = n번째 집까지 털었을때 돈의 최댓값
dp[n] = max(dp[n-1], dp[n-2]+money[n])

1. 첫번째 집 텀 -> 마지막 집 못텀
2. 두번째 집 텀 -> 첫번째 집 못텀

1. 첫번째 집 텀 가정
dp[1]=1
dp[2]=2
dp[3]=max(2, 1+3)=4

2. 첫번째 집 텀X 가정
dp[2]=2
dp[3]=max(2, 0+3)=3
dp[4]=max(3, 2+1)=3

집: 3개 이상 1,000,000개 이하인 정수
money 값: 0 이상 1,000 이하인 정수
'''