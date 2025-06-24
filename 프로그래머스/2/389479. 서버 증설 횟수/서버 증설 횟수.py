def solution(players, m, k):
    answer = 0
    cur = 0
    returns = dict()
    
    for i, player in enumerate(players):
        if i in returns:
            cur -= returns[i]
        
        if player == 0:
            continue
        
        need, mod = divmod(player, m)
        if need > cur:
            answer += (need-cur)
            returns[i+k] = (need-cur)
            cur = need
            
    return answer