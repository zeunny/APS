import collections, bisect

max_word_len = 0

def check(word, words):
    start = word + 'a'
    end = word + 'z'*(max_word_len-1)

    return bisect.bisect_right(words, end) - bisect.bisect_left(words, start)

def solution(words):
    global max_word_len
    
    answer = 0
    visited = collections.defaultdict(int)

    words.sort()
    for word in words:
        if len(word) > max_word_len:
            max_word_len = len(word)
    
    for word in words:
        check_word = ''
        for i in range(len(word)-1):
            check_word += word[i]
            
            if visited[check_word]:
                continue
            
            visited[check_word] = 1
            cnt = check(check_word, words)

            if cnt == 1:
                answer += i+1
                break
        else:
            visited[word] = 1
            answer += len(word)
            
    return answer