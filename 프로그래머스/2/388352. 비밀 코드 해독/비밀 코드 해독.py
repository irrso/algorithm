from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    for comb in combinations(range(1, n+1), 5):
        is_possible = True
        for question, system in zip(q, ans):
            if len(set(question) & set(comb)) != system:
                is_possible = False
                break
        if is_possible:
            answer += 1
                
    return answer