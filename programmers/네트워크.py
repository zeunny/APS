import collections

def solution(n, computers):
    answer = 0
    graph = collections.defaultdict(list)
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
    
    def network(computer):
        if check[computer]:
            return
        check[computer] = True
        while graph[computer]:
            network(graph[computer].pop())
    
    check = [False]*n
    for computer in range(n):
        if check[computer]:
            continue
        network(computer)
        answer += 1
                
    return answer