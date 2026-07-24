def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, n, computers)
            answer += 1

    return answer


def dfs(node, visited, n, computers):
    visited[node] = True
    
    for nxt_node in range(n):
        if computers[node][nxt_node]==1 and not visited[nxt_node]:
            dfs(nxt_node, visited, n, computers)


'''
네트워크의 개수
- A와 B연결, B와 C연결 -> A와 C연결 -> A, B, C는 같은 네트워크

dfs

n: 컴퓨터 개수 1~200
각 컴퓨터: 0~(n-1)
computers[i][j]: 1이면 i, j번 컴퓨터 연결
'''