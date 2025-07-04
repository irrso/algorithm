def solution(lottos, win_nums):
    answer = []
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5}
    
    not_known = lottos.count(0)
    corr = sum(1 for lotto in lottos if lotto in win_nums)
    
    answer.append(ranking[corr+not_known] if corr+not_known in ranking else 6)
    answer.append(ranking[corr] if corr in ranking else 6)

    return answer