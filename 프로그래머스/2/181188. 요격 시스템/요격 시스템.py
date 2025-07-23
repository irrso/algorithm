def solution(targets):
    answer = 0
    bef = 0
    
    for target in sorted(targets, key=lambda x: x[1]):
        if bef > target[0]:
            continue

        bef = target[1]
        answer += 1
    
    return answer