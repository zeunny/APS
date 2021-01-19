import collections

def solution(n, costs):
    answer, cnt = 0, 1
    graph = collections.defaultdict(list)
    
    for s, e, c in costs:
        graph[s].append((e,c))
        graph[e].append((s,c))
    
    check = [False]*n
    check[0] = True
    while cnt < n:
        minV, u = float('inf'), -1
        for i in range(len(check)):
            if not check[i]:
                continue
            for e, c in sorted(graph[i], key=lambda x: x[1]):
                if check[e]:
                    continue
                if c < minV:
                    minV = c
                    u = e
        check[u] = True
        answer += minV
        cnt += 1
            
    return answer