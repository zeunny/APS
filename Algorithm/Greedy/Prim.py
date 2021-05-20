"""
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

결과
key
[0, 21, 31, 34, 46, 18, 25]
p
[-1, 2, 0, 4, 2, 3, 2]
result
175
"""

V, E = map(int,input().split())
adj = [[0]*V for _ in range(V)]

for i in range(E):
    s, e, c = map(int,input().split())
    adj[s][e] = c
    adj[e][s] = c

# key, p, mst 준비
INF = float('inf')
key = [INF]*V
p = [-1]*V
mst = [False]*V

# 시작점 선택 : 0번 선택
key[0] = 0
cnt = 0
result = 0
while cnt < V:
    # 아직 mst가 아니고 key가 최소인 정점 선택 : u
    min = INF
    u = -1
    for i in range(V):
        if not mst[i] and key[i] < min:
            min = key[i]
            u = i
    # u를 mst로 선택
    mst[u] = True
    result += min
    cnt += 1
    # key 값을 갱신
    # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
    for w in range(V):
        if adj[u][w] and not mst[w] and key[w] > adj[u][w]:
            key[w] = adj[u][w]
            p[w] = u

print(key)
print(p)
print(result)