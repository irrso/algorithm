def solution(sticker):
    N = len(sticker)
    
    if N == 1:
        return sticker[0]
    
    dp1 = [0]*N
    dp1[0] = sticker[0]
    for n in range(1, N-1):
        dp1[n] = max(dp1[n-2]+sticker[n], dp1[n-1])
    
    dp2 = [0]*N
    for n in range(1, N):
        dp2[n] = max(dp2[n-2]+sticker[n], dp2[n-1])
    
    return max(dp1[-2], dp2[-1])


'''
뜯어낸 스티커에 적힌 숫자의 합이 최대
- 뜯어낸 양쪽 인접한 스티커는 사용X
- 스티커 배열의 첫 원소 마지막 원소 연결됨

스티커 길이 N: 1~100,000
칸 숫자: 1~100

dp[n] = n번째 숫자까지 골랐을때 최대의 합
dp[n] = max(dp[n-2]+sticker[n], dp[n-1])
'''