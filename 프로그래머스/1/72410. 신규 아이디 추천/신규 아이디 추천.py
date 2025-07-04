def solution(new_id):
    answer = ''
    n = len(new_id)

    new_id = new_id.lower()
    is_conti = False
    for i, ch in enumerate(new_id):
        if answer == '' and ch == '.':
            continue
        
        if ch.isalpha() or ch.isdigit() or ch == '-' or ch == '_':
            answer += ch
            is_conti = False
        
        if ch == '.' and not is_conti:
            answer += ch
            is_conti = True
    
    if answer != '' and answer[-1] == '.':
        answer = answer[:-1]
    
    if answer == '':
        answer = 'a'

    n = len(answer)
    if n >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif n <= 2:
        ch = answer[-1]
        for _ in range(3-n):
            answer += ch
            
    return answer