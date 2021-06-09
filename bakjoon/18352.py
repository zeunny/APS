# def Floyd(G, n):
#   inf = float('inf')
#   D = [[inf]*(n+1) for _ in range(n+1)]

#   for i in range(1, n+1):
#     D[i][i] = 0

#   for s, e, c in G:
#     D[s][e] = c

#   for k in range(1, n+1):
#     for i in range(1, n+1):
#       for j in range(1, n+1):
#         if D[i][j] > D[i][k] + D[k][j]:
#           D[i][j] = D[i][k] + D[k][j]

#   return D

# def Diikstra(V, E):
#   INF = float('inf')
#   graph = {i: [] for i in range(V+1)}

#   for s, e, c in E:
#     graph[s].append([e, c])
  
#   dist = [INF]*(V+1)
#   selected = [False]*(V+1)

#   dist[1] = 0
#   cnt = 0
#   while cnt < V:
#     min_index, min_value = 0, INF
#     for i, v in enumerate(dist):
#       if v < min_value and not selected[i]:
#         min_index = i
#         min_value = v
    
#     selected[min_index] = True
#     cnt += 1
#     for i, c in graph[min_index]:
#       dist[i] = min(dist[i], dist[min_index]+c)

#   return dist

import sys

input = sys.stdin.readline

N, M, K, X = map(int,input().split())

INF = float('inf')
graph = {i: [] for i in range(N+1)}

for _ in range(M):
  s, e = map(int,input().split())
  graph[s].append([e, 1])

dist = [INF]*(N+1)
selected = [False]*(N+1)

dist[1] = 0
cnt = 0
while cnt < N:
  min_index, min_value = 0, INF
  for i, v in enumerate(dist):
    if v < min_value and not selected[i]:
      min_index = i
      min_value = v
  
  selected[min_index] = True
  cnt += 1
  for i, c in graph[min_index]:
    dist[i] = min(dist[i], dist[min_index]+c)

answer = []

for i, v in enumerate(dist):
  if v == K:
    print(i)