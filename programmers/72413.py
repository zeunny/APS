import collections

def solution(n, s, a, b, fares):
    INF = float('inf')
    answer = INF
    
    graph = collections.defaultdict(list)
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    # a
    a_cost = [INF]*(n+1)
    a_cost[a] = 0
    q = collections.deque([a])
    while q:
        u = q.popleft()
        for w, cost in graph[u]:
            if a_cost[w] > a_cost[u] + cost:
                a_cost[w] = a_cost[u] + cost
                q.append(w)
    
    # b
    b_cost = [INF]*(n+1)
    b_cost[b] = 0
    q = collections.deque([b])
    while q:
        u = q.popleft()
        for w, cost in graph[u]:
            if b_cost[w] > b_cost[u] + cost:
                b_cost[w] = b_cost[u] + cost
                q.append(w)
    
    # s
    s_cost = [INF]*(n+1)
    s_cost[s] = 0
    q = collections.deque([s])
    while q:
        u = q.popleft()
        for w, cost in graph[u]:
            if s_cost[w] > s_cost[u] + cost:
                s_cost[w] = s_cost[u] + cost
                q.append(w)
                
    for i in range(1,n+1):
        answer = min(answer, a_cost[i] + b_cost[i] + s_cost[i])
            
    return answer