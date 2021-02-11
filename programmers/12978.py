def solution(N, road, K):
    answer = 0

    graph = {i: [] for i in range(N+1)}
    for s, e, d in road:
        graph[s].append((e,d))
        graph[e].append((s,d))
    
    INF = float('inf')
    dist = [INF]*(N+1)
    selected = [False]*(N+1)
    
    dist[1] = 0
    cnt = 0
    while cnt < N:
        minV = INF
        u = -1
        for i in range(1,N+1):
            if not selected[i] and dist[i] < minV:
                minV = dist[i]
                u = i
        
        selected[u] = True
        cnt += 1
        for w, cost in graph[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    for i in range(1,N+1):
        if dist[i] <= K:
            answer += 1
            
    return answer