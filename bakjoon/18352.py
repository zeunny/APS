def Floyd(G, n):
  inf = float('inf')
  D = [[inf]*(n+1) for _ in range(n+1)]

  for i in range(1, n+1):
    D[i][i] = 0

  for s, e, c in G:
    D[s][e] = c

  for k in range(1, n+1):
    for i in range(1, n+1):
      for j in range(1, n+1):
        if D[i][j] > D[i][k] + D[k][j]:
          D[i][j] = D[i][k] + D[k][j]

  return D

import sys

input = sys.stdin.readline

N, M, K, X = map(int,input().split())

G = []

for _ in range(M):
  s, e = map(int,input().split())
  G.append((s, e, 1))

D = Floyd(G, N)

answer = []

for i, v in enumerate(D[X]):
  if v == K:
    answer.append(i)

if answer:
  print(*answer, sep="\n")
else:
  print(-1)