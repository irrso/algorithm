from itertools import combinations


def solution(orders, course):
    answer = []
    cases = set()
    courses = [[] for _ in range(course[-1]+1)]
    
    for order in orders:
        n = len(order)
        for i in range(2, n+1):
            [cases.add(''.join(sorted(comb))) for comb in combinations(order, i)]
            
    for case in list(cases):
        i = len(case)
        cnt = sum([1 for order in orders if all(ch in order for ch in case)])
        if i in course and cnt >= 2:
            if courses[i] == [] or cnt == courses[i][0][1]:
                courses[i].append((case, cnt))
            elif cnt > int(courses[i][0][1]):
                courses[i] = [(case, cnt)]
        
    for i in course:
        for ans in courses[i]:
                answer.append(ans[0])
                
    return sorted(answer)