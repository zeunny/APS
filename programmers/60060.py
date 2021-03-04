import collections, bisect

def search(lst, query):
    start = query.replace('?', 'a')
    end = query.replace('?', 'z')
    left = bisect.bisect_left(lst[len(query)], start)
    right = bisect.bisect_right(lst[len(query)], end)
    return right - left
    
def solution(words, queries):
    answer = []
    visited = {}
    words_dict = collections.defaultdict(list)
    reverse_words_dict = collections.defaultdict(list)
    
    for word in words:
        words_dict[len(word)].append(word)
        reverse_words_dict[len(word)].append(word[::-1])
    
    for value in words_dict.values():
        value.sort()
        
    for value in reverse_words_dict.values():
        value.sort()
    
    for query in queries:
        if query.count('?') == len(query):
            answer.append(len(words_dict[len(query)]))
            continue
            
        if visited.get(query):
            answer.append(visited[query])
        else:
            if query[-1] == '?':
                count = search(words_dict, query)
            else:
                count = search(reverse_words_dict, query[::-1])
                
            answer.append(count)
            visited[query] = count
            
    return answer