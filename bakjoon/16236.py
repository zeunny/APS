import sys, collections

input = sys.stdin.readline

N = int(input())

space = []
for _ in range(N):
  space.append(list(map(int,input().split())))

baby_shark = 2
queue = collections.deque([])
visited = [[0]*N for _ in range(N)]
for r in range(N):
  for c in range(N):
    if space[r][c] == 9:
      queue.append((r,c,0))
      visited[r][c] = 1
      space[r][c] = 0

directions = {(0,1),(1,0),(-1,0),(0,-1)}
answer, cnt = 0, 0
while queue:
  eat = []
  for _ in range(len(queue)):
    r, c, time = queue.popleft()
    for d in directions:
      nr, nc = r+d[0], c+d[1]
      if 0 <= nr < N and 0 <= nc < N and space[nr][nc] <= baby_shark and not visited[nr][nc]:
        if 0 < space[nr][nc] < baby_shark:
          eat.append((nr,nc, time+1))
        visited[nr][nc] = 1
        queue.append((nr,nc, time+1))
  if eat:
    eat.sort()
    eat_r, eat_c, eat_time = eat[0]
    answer += eat_time
    space[eat_r][eat_c] = 0
    visited = [[0]*N for _ in range(N)]
    queue = collections.deque([(eat_r,eat_c,0)])
    visited[eat_r][eat_c] = 1
    cnt += 1
    if cnt == baby_shark:
      baby_shark += 1
      cnt = 0

print(answer)