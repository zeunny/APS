import re, collections, itertools

def solution(info, query):
    answer = []
    info_hash = collections.defaultdict(list)
    for v in info:
        arr = v.split()
        condition, score = tuple(arr[:-1]), int(arr[-1])
        info_hash[()].append(score)
        info_hash[condition].append(score)
        for n in range(1,4):
            for com in itertools.combinations(condition, n):
                info_hash[com].append(score)
    
    for key in info_hash.keys():
        info_hash[key].sort()
    
    for v in query:
        arr = v.replace('and', '').replace('-', '').split()
        condition, score = tuple(arr[:len(arr)-1]), int(arr[-1])
        scores = info_hash[condition]
        
        if len(scores) == 0:
            answer.append(0)
        else:
            left, right = 0, len(scores)-1
            while left <= right:
                middle = (left + right) // 2
                if scores[middle] >= score:
                    right = middle - 1
                else:
                    left = middle + 1

            if scores[middle] >= score:
                answer.append(len(scores) - middle)
            else:
                answer.append(len(scores) - middle - 1)
        
    return answer