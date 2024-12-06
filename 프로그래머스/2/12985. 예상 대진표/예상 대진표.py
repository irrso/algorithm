def round(lists, answer):
    winners = []
    for i in range(0, len(lists), 2):
        if lists[i] and lists[i+1]:
            return answer
        winners.append(lists[i] or lists[i+1])
    
    answer += 1
    return round(winners, answer)


def solution(n,a,b):
    answer = 1 
    lists = [True if (i == a) or (i == b) else False for i in range(1, n+1)]
    
    return round(lists, answer)