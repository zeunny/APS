import collections

def solution(dirs):
    answer = 0
    directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    visited = collections.defaultdict(set)
    
    current = [0, 0]
    for d in dirs:
        i, j = directions[d]
        new_i = current[0] + i
        new_j = current[1] + j
        
        if -5 <= new_i <= 5 and -5 <= new_j <= 5:
            if directions[d] not in visited[(new_i, new_j)]:
                answer += 1
            
            visited[(new_i, new_j)].add(directions[d])
            visited[tuple(current)].add((-directions[d][0], -directions[d][1]))
            current = [new_i, new_j]
    
    return answer