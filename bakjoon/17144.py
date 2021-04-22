import sys, copy

input = sys.stdin.readline

R, C, T = map(int,input().split())

rooms = []
for _ in range(R):
  rooms.append(list(map(int,input().split())))

directions = {(0,1),(1,0),(0,-1),(-1,0)}
new_rooms = [[0]*C for _ in range(R)]

def diffuse(r, c):
  cnt = 0
  for d in directions:
    nr = r+d[0]
    nc = c+d[1]
    if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] != -1:
      new_rooms[nr][nc] += rooms[r][c]//5
      cnt += 1
  new_rooms[r][c] += rooms[r][c] - (rooms[r][c] // 5 * cnt)

air_purifier = []
purify_directions = {'top': [(0,1), (-1,0), (0,-1), (1,0)], 'bottom': [(0,1), (1,0), (0,-1),(-1,0)]}
def purify(position, air_purifier):
  directions = purify_directions[position]
  r, c = air_purifier
  save = 0
  for d in directions:
    r += d[0]
    c += d[1]
    while 0 <= r < R and 0 <= c < C and (r, c) != air_purifier:
      save, new_rooms[r][c] = new_rooms[r][c], save
      r += d[0]
      c += d[1]
    else:
      r -= d[0]
      c -= d[1]

for r in range(R):
  for c in range(C):
    if rooms[r][c] == -1:
      air_purifier.append((r,c))
air_purifier.sort()

while T > 0:
  for r in range(R):
    for c in range(C):
      if rooms[r][c] > 0:
        diffuse(r, c)

  air_purifier.sort()
  purify('top', air_purifier[0])
  purify('bottom', air_purifier[1])

  rooms = copy.deepcopy(new_rooms)
  for i, j in air_purifier:
    rooms[i][j] = -1

  new_rooms = [[0]*C for _ in range(R)]
  T -= 1

answer = 0
for r in range(R):
  for c in range(C):
    if rooms[r][c] > 0:
      answer += rooms[r][c]

print(answer)