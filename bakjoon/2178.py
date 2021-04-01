import sys, heapq

input = sys.stdin.readline

N, M = map(int,input().split())

maze = []
for _ in range(N):
  maze.append(list(map(int,input().rstrip('\n'))))

directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
visited = [[0]*M for _ in range(N)]
heap = []

heapq.heappush(heap, (1, 0, 0))
visited[0][0] = 1

while heap:
  cnt, i, j = heapq.heappop(heap)

  if (i, j) == (N-1, M-1):
    print(cnt)
    break
  
  for d in directions:
    ni = i + d[0]
    nj = j + d[1]

    if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] and not visited[ni][nj]:
      heapq.heappush(heap, (cnt+1, ni, nj))
      visited[ni][nj] = 1