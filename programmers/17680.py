import collections

def solution(cacheSize, cities):
    answer = 0
    cache_hash = collections.defaultdict(int)
    time = 1
    for city in cities:
        city = city.lower()
        if cache_hash[city] == 0:
            answer += 5
        else:
            if time - cache_hash[city] <= cacheSize:
                answer += 1
                for key in cache_hash.keys():
                    if cache_hash[key] < cache_hash[city]:
                        cache_hash[key] += 1
            else:
                answer += 5
        cache_hash[city] = time
        time += 1
    
    return answer