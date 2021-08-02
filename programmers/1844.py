from collections import deque

def solution(maps):
    answer = 0
    directions = {(0,1), (1,0), (0,-1), (-1,0)}
    
    N, M = len(maps), len(maps[0])
    q = deque([(0,0)])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    
    while q:
        answer += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == N-1 and j == M-1:
                return answer
            
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
        
    return -1