from itertools import combinations

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    for i in range(n):
        for comb in combinations(range(n), i):
            nums = numbers.copy()
            for c in comb:
                nums[c] = -nums[c]
                
            if sum(nums) == target:
                answer += 1
    
    return answer


'''
타겟 넘버 만드는 방법의 수
- 정수의 순서를 바꾸지 않고 더하거나 뺌

n: 2~20
각 숫자: 1~50 자연수
타겟 넘버: 1~1000 자연수
'''