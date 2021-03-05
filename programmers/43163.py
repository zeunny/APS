import sys

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def DFS(word, count):
        nonlocal minV
        if count >= minV:
            return
        if word == target:
            if count < minV:
                minV = count
        for i in range(len(words)):
            if check[i]:
                continue
            for k in range(len(begin)):
                if word[k] != words[i][k]:
                    if k == len(words)-1 or word[k+1:] == words[i][k+1:]:
                        check[i] = True
                        DFS(words[i], count+1)
                        check[i] = False
                    else:
                        break
    
    minV = sys.maxsize
    check = [False]*len(words)
    DFS(begin, 0)
    
    return minV