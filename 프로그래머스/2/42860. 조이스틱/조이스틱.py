def solution(name):
    answer = 0

    for n in name:
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)

    idx = 0
    move = len(name)-1
    for i, n in enumerate(name):
        if n == 'A':
            idx = i

            while idx < len(name) and name[idx]=='A':
                idx += 1

            left = (i-1 if i else i)
            right = len(name)-idx
            move = min(move, left+right+min(left, right))

    answer += move
    return answer