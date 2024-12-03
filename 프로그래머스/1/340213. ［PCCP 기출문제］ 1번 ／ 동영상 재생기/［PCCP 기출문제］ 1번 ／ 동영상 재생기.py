def sec(time):
    return int(time[:2])*60 + int(time[3:])

def solution(video_len, pos, op_start, op_end, commands):
    video_len = sec(video_len)
    op_start = sec(op_start)
    op_end = sec(op_end)
    pos = op_end if (op_start <= sec(pos) <= op_end) else sec(pos)
    
    for command in commands:
        if command == 'prev':
            pos = pos-10 if pos-10 >= 0 else 0
        else:
            pos = pos+10 if pos+10 < video_len else video_len 
        
        pos = op_end if (op_start <= pos <= op_end) else pos
    
    minute, second = int(pos/60), int(pos%60)
    answer = f'{minute:02d}:{second:02d}'

    return answer