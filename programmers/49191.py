import collections

def solution(n, results):
    know_ranking = [False]*(n+1)
    win_graph = collections.defaultdict(list)
    lose_graph = collections.defaultdict(list)
    
    for A, B in results:
        win_graph[A].append(B)
        lose_graph[B].append(A)

    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            know_ranking[i] = True
            continue
        
        win_stack, lose_stack = [i], [i]
        win_visited, lose_visited = [False]*(n+1), [False]*(n+1)
        
        while win_stack:
            player = win_stack.pop()
            win_visited[player] = True
            for s in win_graph[player]:
                if not win_visited[s]:
                    win_stack.append(s)
        win_visited[i] = False
        
        while lose_stack:
            player = lose_stack.pop()
            lose_visited[player] = True
            for s in lose_graph[player]:
                if not lose_visited[s]:
                    lose_stack.append(s)
        lose_visited[i] = False
                    
        if sum(win_visited) + sum(lose_visited) == n-1:
            know_ranking[i] = True
        
    return sum(know_ranking)