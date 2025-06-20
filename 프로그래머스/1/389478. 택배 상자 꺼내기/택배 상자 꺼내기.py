def solution(n, w, num):
    answer = 1
    
    while(True):
        div, mod = divmod(num, w)
    
        if mod == 0:
            num += 1
        else:
            num += 2*(w-mod)+1
            
        if n < num:
            break
            
        answer += 1

    return answer

