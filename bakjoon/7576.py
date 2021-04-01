import sys, collections

input = sys.stdin.readline

M, N = map(int,input().split())

empty_cnt = 0
queue = collections.deque([])
tomatos = []
visited = [[0]*M for _ in range(N)]

for n in range(N):
  tomatos.append(list(map(int,input().split())))

  for index, tomato in enumerate(tomatos[-1]):
    if tomato == -1:
      empty_cnt += 1
    elif tomato == 1:
      queue.append((n, index))
      visited[n][index] = 1

total_cnt = M*N - empty_cnt

directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
tomato_cnt, days = 0, 0

while queue:
  tomato_cnt += len(queue)
  days += 1

  for _ in range(len(queue)):
    r, c = queue.popleft()

    for d in directions:
      nr = r + d[0]
      nc = c + d[1]
      if 0 <= nr < N and 0 <= nc < M and not tomatos[nr][nc] and not visited[nr][nc]:
        queue.append((nr, nc))
        tomatos[nr][nc] = 1
        visited[nr][nc] = 1

if tomato_cnt == total_cnt:
  print(days-1)
else:
  print(-1)