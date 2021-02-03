def solution(gems):
    answer = [0,100000]
    
    gems_set = set()
    gems_len = len(set(gems))
    gems_hash = {}
    
    start_index = 0
    
    for i, gem in enumerate(gems):
        if gems_hash.get(gem) == None:
            gems_set.add(gem)
        else:
            while start_index < i and gems[start_index] == gem:
                start_index += 1
                
            if start_index < gems_hash[gems[start_index]]:
                for j in range(start_index+1, gems_hash[gems[start_index]]+1):
                    if j == gems_hash[gems[j]]:
                        start_index = j
                        break
                else:
                    start_index = gems_hash[gems[start_index]]
            
        if len(gems_set) == gems_len:
            if i - start_index < answer[1] - answer[0]:
                answer = [start_index+1, i+1]
                    
        gems_hash[gem] = i
    
    return answer