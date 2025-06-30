def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    for term in terms:
        a, b = term.split()
        term_dict[a] = int(b)
        
    for i, pravacy in enumerate(privacies):
        dates, term = pravacy.split()
        
        year, month, date = dates.split('.')
        year, month, date = int(year), int(month), int(date)
        
        month += term_dict[term]
        year += (month-1)//12
        month = (month-1)%12 + 1
        
        tyear, tmonth, tdate = today.split('.')
        tyear, tmonth, tdate = int(tyear), int(tmonth), int(tdate)
        
        if (year, month, date) <= (tyear, tmonth, tdate):
            answer.append(i+1)
        
    return answer