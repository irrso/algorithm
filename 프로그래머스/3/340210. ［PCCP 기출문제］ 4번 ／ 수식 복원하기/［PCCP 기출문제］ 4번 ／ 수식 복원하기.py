def to_base(n, base):
    num = ''
    if n == 0:
        return 0
    
    while n > 0:
        n, mod = divmod(n, base)
        num += str(mod)
    
    return int(num[::-1])


def solution(expressions):
    answer = []
    bases = None

    nums = set()
    for expression in expressions:
        expression = list(map(str, expression.split()))
        a, b = int(expression[0]), int(expression[2])
        nums.add(a)
        nums.add(b)
    
    for expression in sorted(expressions, key=lambda x: x[-1]):
        expression = list(map(str, expression.split()))
        a, b, c = expression[0], expression[2], expression[4]
        operator = expression[1]
        
        if c != 'X':
            temp = set()
            for q in range(2, 10):
                try:
                    if operator == '+':
                        if int(a, q) + int(b, q) == int(c, q):
                            temp.add(q)
                    else:
                        if int(a, q) - int(b, q) == int(c, q):
                            temp.add(q)
                except:
                    continue
            
            if bases is None:
                bases = temp
            else:
                bases = bases & temp
            continue
        
        if bases is None:
            c = None
            result = set()
            for q in range(2, 10):
                try:
                    for num in nums:
                        int(str(num), q)
                except:
                    continue
                    
                try:
                    if operator == '+':
                        temp_c = int(a, q) + int(b, q)
                    else:
                        temp_c = int(a, q) - int(b, q)
                except:
                    continue
                
                try:
                    temp_c = to_base(temp_c, q)
                    if c is None:
                        c = temp_c
                        result.add(c)
                    else:
                        if c != temp_c:
                            result = set()
                            break
                except:
                    continue
        else:
            result = set()
            for base in bases:
                try:
                    for num in nums:
                        int(str(num), base)
                except:
                    continue
                    
                try:
                    if operator == '+':
                        c = int(a, base) + int(b, base)
                    else:
                        c = int(a, base) - int(b, base)
                    result.add(to_base(c, base))
                except:
                    result = set()
                    break 
    
        if len(result) == 1:
            ans = f'{a} {operator} {b} = {result.pop()}'
        else:
            ans = f'{a} {operator} {b} = ?'
            
        answer.append(ans)

    return answer