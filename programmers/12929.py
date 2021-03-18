answer = 0

def search(n, k, left_bracket, right_bracket):
    global answer
    if k == n:
        answer += 1
        return
    
    if k-right_bracket < n//2:
        search(n, k+1, left_bracket+1, right_bracket)
    if left_bracket > 0:
        search(n, k+1, left_bracket-1, right_bracket+1)

def solution(n):
    search(n*2, 1, 1, 0)
    return answer