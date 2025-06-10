def solution(data, ext, val_ext, sort_by):
    answer = []
    order = dict()
    order['code'], order['date'], order['maximum'], order['remain'] = 0, 1, 2, 3
    
    for data in data:
        if data[order[ext]] < val_ext:
            answer.append(data)
    
    answer = sorted(answer, key=lambda x: x[order[sort_by]])
    return answer