from itertools import product

def solution(users, emoticons):
    answer = []
    n, m = len(users), len(emoticons)
        
    for discount in product([10, 20, 30, 40], repeat=m):
        membership, tot_price = 0, 0
        
        for percent, price in users:
            user_price = 0
            
            for em_percent, em_price in zip(discount, emoticons):
                if em_percent >= percent:
                    user_price += em_price*((100-em_percent)/100)
                    
            if user_price >= price:
                membership += 1
            else:
                tot_price += user_price
        
        answer = max(answer, [membership, tot_price])
                
    return answer