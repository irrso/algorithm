from itertools import product
from bisect import bisect_left

def solution(info, query):
    answer = []
    db = dict()

    for apply in info:
        apply = apply.split()
        apply, score = apply[:-1], int(apply[-1])
        
        lists = [(a, '-') for a in apply]
        for case in product(*lists):
            case = ''.join(case)
            if case not in db:
                db[case] = [score]
            else:
                db[case].append(score)
    
    for scores in db.values():
        scores.sort()
    
    for q in query:
        q = q.replace('and', '')
        q = q.split()
        q, score = ''.join(q[:-1]), int(q[-1])
        
        if q in db:
            idx = bisect_left(db[q], score)
            answer.append(len(db[q])-idx)
        else:
            answer.append(0)
        
    return answer