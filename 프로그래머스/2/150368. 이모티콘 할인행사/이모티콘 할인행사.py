from itertools import product

def solution(users, emoticons):
    answer = []
    n, m = len(users), len(emoticons)
        
    for i, discount in enumerate(product([10, 20, 30, 40], repeat=m)):
        membership, tot_price = 0, 0
        
        for user in users:
            percent, price = user
            em_price = 0
            
            for dc, emoticon in zip(discount, emoticons):
                if dc >= percent:
                    em_price += emoticon*((100-dc)/100)
                    
            if em_price >= price:
                membership += 1
            else:
                tot_price += em_price
        
        if i == 0:
            answer = [membership, tot_price]
            continue
        
        if answer[0] < membership:
            answer = [membership, tot_price]
        elif answer[0] == membership and answer[1] < tot_price:
            answer = [membership, tot_price]
                
    return answer