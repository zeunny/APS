import sys, collections

input = sys.stdin.readline

N, L, R = map(int,input().split())
conturies = []

for _ in range(N):
  conturies.append(list(map(int,input().split())))

directions = {(0,1),(1,0),(-1,0),(0,-1)}
cnt = 0

while True:
  group = collections.defaultdict(list)
  visited = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        queue = collections.deque([(i, j)])
        move = set()
        visited[i][j] = 1

        while queue:
          y, x = queue.popleft()
          move.add((y, x))
          for d in directions:
            ni = y+d[0]
            nj = x+d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(conturies[y][x]-conturies[ni][nj]) <= R:
              queue.append((ni, nj))
              visited[ni][nj] = 1
        
        if len(move) > 1:
          group[(i, j)].extend(list(move))
  
  if not group.keys():
    break

  for key in group.keys():
    people = 0
    for value in group[key]:
      people += conturies[value[0]][value[1]]

    for value in group[key]:
      conturies[value[0]][value[1]] = people // len(group[key])
  
  cnt += 1
          
print(cnt)