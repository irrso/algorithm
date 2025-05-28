def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    max_health = health
    cons = 0
    
    for i in range(1, attacks[-1][0]+1):
        for attack in attacks:
            time, damage = attack[0], attack[1]
            if i == time:
                cons = 0
                health -= damage
                if health <= 0:
                    return -1
                break
        
        if i != time:
            cons += 1
            if cons == t:
                health += y
                cons = 0
            health += x
            if health > max_health:
                health = max_health
    
    return health