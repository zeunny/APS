def Floyd(V, E):   # V: 간선의 수, E: 노드 (s, e, c) s와 e가 연결되어있고 거리는 c라고 가정
  INF = float('inf')
  D = [[INF]*(V+1) for _ in range(V+1)]
  for s, e, c in E:
    D[s][e] = c

  for i in range(1, V+1):
    D[i][i] = 0

  for k in range(1, V+1):
    for i in range(1, V+1):
      for j in range(1, V+1):
        D[i][j] = min(D[i][j], D[i][k]+D[k][j])