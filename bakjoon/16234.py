import sys, collections

input = sys.stdin.readline

N, L, R = map(int,input().split())
conturies = []

for _ in range(N):
  conturies.append(list(map(int,input().split())))

directions = {(0,1),(1,0),(-1,0),(0,-1)}
visited = [[0]*N for _ in range(N)]
cnt = 0

while True:
  parent = [[False]*N for _ in range(N)]
  group = collections.defaultdict(list)
  visited = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        queue = collections.deque([(i, j)])
        move = set()

        while queue:
          # print('queue :', queue, i, j)
          y, x = queue.popleft()
          visited[y][x] = 1
          move.add((y, x))
          # print('move :', move, i, j)
          for d in directions:
            ni = y+d[0]
            nj = x+d[1]
            # print(y, x, ni, nj)
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(conturies[y][x]-conturies[ni][nj]) <= R:
              queue.append((ni, nj))
        
        if len(move) > 1:
          # print('move :', move, i, j)
          group[(i, j)].extend(list(move))
  
  if not group.keys():
    break

  # print(group)

  for key in group.keys():
    people = 0
    for value in group[key]:
      # print('value :', value)
      people += conturies[value[0]][value[1]]

    for value in group[key]:
      conturies[value[0]][value[1]] = people // len(group[key])
  
  # print(conturies)
  cnt += 1
          
print(cnt)