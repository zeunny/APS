import collections

def solution(n, edge):
    count = [0]*(n+1)
    visited = [False]*(n+1)
    maxV = 0

    graph = collections.defaultdict(list)
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    queue = collections.deque([(1, 1)])
    visited[1] = True
    
    while queue:
        start, cnt = queue.popleft()
        visited[start] = True
        for s in graph[start]:
            if not visited[s]:
                count[cnt] += 1
                if cnt > maxV:
                    maxV = cnt
                visited[s] = True
                queue.append((s, cnt+1))

    return count[maxV]