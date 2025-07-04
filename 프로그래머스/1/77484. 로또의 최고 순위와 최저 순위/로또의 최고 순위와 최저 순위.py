def solution(lottos, win_nums):
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    not_known = lottos.count(0)
    corr = sum(1 for lotto in lottos if lotto in win_nums)

    return ranking[corr+not_known], ranking[corr]