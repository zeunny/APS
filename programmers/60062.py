import itertools

def solution(n, weak, dist):
    if len(weak) == 1:
        if len(dist) >= 1:
            return 1
        
    for k in range(1, len(dist)+1):
        for c in itertools.combinations(dist, k):
            for p in itertools.permutations(c):
                for m in range(len(weak)):
                    new_weak = weak[m:] + list(map(lambda x: x+n, weak[:m]))
                    
                    p_copy = list(p)
                    p_index, w_index = 0, 1
                    while w_index < len(new_weak) and p_index < len(p_copy):
                        if new_weak[w_index] - new_weak[w_index-1] <= p_copy[p_index]:
                            p_copy[p_index] -= new_weak[w_index] - new_weak[w_index-1]
                        else:
                            p_index += 1
                        w_index += 1
                        
                    if p_index < len(p) and w_index == len(new_weak):
                        return len(p)
                    
    return -1