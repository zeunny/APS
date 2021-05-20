'''
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6

[0, 3, 5, 9, 11, 12]
'''

V, E = map(int,input().split())
adj = {i:[] for i in range(V)}

for _ in range(E):
    s, e, c = map(int,input().split())
    adj[s].append([e,c])

INF = float('inf')
# dist, selected 배열 준비
dist = [INF]*V
selected = [False]*V

# 시작점 선택
dist[0] = 0
cnt = 0
while cnt < V:
    # dist가 최소인 정점 찾기
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1
    # 간선완화
    for w, cost in adj[u]: # 도착정점, 가중치
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost

print(dist)