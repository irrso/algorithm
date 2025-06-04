def solution(board, h, w):
    answer = 0
    n = len(board)
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    
    for y, x in zip(dy, dx):
        ny, nx = y+h, x+w
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == board[h][w]:
            answer += 1
    
    return answer