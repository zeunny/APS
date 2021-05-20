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

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
      return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

V, E = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(E)]

# 간선을 간선가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])
# make_set : 모든 정점에 대해 집합 생성
p = [0]*V
rank = [0]*V
for i in range(V):
    make_set(i)

cnt = result = 0; mst = []
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지
for i in range(E):
    s, e, c = edges[i]
    # 사이클이면 건너뛰기 : 간선의 두 정점이 서로 같은 집합이면 => find_set
    if find_set(s) == find_set(e):
      continue
    # 간선 선택
    result += c
    # => mst에 간선 정보 더하기 / 두 정점을 합친다 => union
    mst.append(edges[i])
    union(s, e)
    cnt += 1
    if cnt == (V-1):
      break