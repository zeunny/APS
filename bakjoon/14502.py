import sys, itertools, copy

input = sys.stdin.readline

N, M = map(int,input().split())

directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

def search_safe_area(lab, viruses, com):
  answer = len(viruses)

  for n, m in com:
    lab[n][m] = 1

  while viruses:
    if answer > min_virus:
      return 0, 0

    i, j = viruses.pop()

    for d in directions:
      ni = i + d[0]
      nj = j + d[1]

      if 0 <= ni < N and 0 <= nj < M and lab[ni][nj] == 0:
        lab[ni][nj] = 2
        answer += 1
        viruses.append((ni, nj))
  
  return N*M - answer - wall_cnt, answer

lab, empty, viruses = [], [], []
wall_cnt = 3

for n in range(N):
  lab.append(list(map(int,input().split())))

  for m in range(M):
    if lab[n][m] == 0:
      empty.append((n, m))
    elif lab[n][m] == 2:
      viruses.append((n, m))
    else:
      wall_cnt += 1

max_value = 0
min_virus = 64

for com in itertools.combinations(empty, 3):
  safe_area_cnt, virus_cnt = search_safe_area(copy.deepcopy(lab), copy.deepcopy(viruses), com)

  if safe_area_cnt > max_value:
    max_value = safe_area_cnt
    min_virus = virus_cnt

print(max_value)