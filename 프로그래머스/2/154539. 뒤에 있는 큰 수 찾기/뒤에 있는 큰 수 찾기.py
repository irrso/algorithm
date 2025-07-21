from collections import deque

def solution(numbers):
    answer = [-1]*len(numbers)
    dq = deque()
    
    for i, num in enumerate(numbers):
        while dq and numbers[dq[-1]] < num:
            idx = dq.pop()
            answer[idx] = num
        
        dq.append(i)
    
    return answer