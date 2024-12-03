def possible(mat, park, i, j):
    for r in range(mat):
        for c in range(mat):
            if park[i+r][j+c] != '-1':
                return False
    return True

def solution(mats, park):
    row, col = len(park), len(park[0])
    
    for mat in sorted(mats, reverse=True):
        for i in range(row-mat+1):
            for j in range(col-mat+1):
                if possible(mat, park, i, j):
                    return mat
    
    return -1