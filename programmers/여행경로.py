import collections

def solution(tickets):
    graph = collections.defaultdict(list)
    for x, y in sorted(tickets, reverse=True):
        graph[x].append(y)
    
    path = []
    def DFS(place):
        while graph[place]:
            DFS(graph[place].pop())
        path.append(place)
    
    DFS('ICN')
    return path[::-1]