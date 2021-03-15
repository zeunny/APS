answer = 0

def n_queen(n, k, column, left_diagonal, right_diagonal):
    global answer
    if k == n:
        answer += 1
        return
    
    for index in range(n):
        if column[index] or left_diagonal[k+index] or right_diagonal[k-index+n-1]:
            continue
        column[index] = 1
        left_diagonal[k+index] = 1
        right_diagonal[k-index+n-1] = 1
        n_queen(n, k+1, column, left_diagonal, right_diagonal)
        column[index] = 0
        left_diagonal[k+index] = 0
        right_diagonal[k-index+n-1] = 0

def solution(n):
    column = [0]*n
    left_diagonal = [0]*(n*2-1)
    right_diagonal = [0]*(n*2-1)
    
    n_queen(n, 0, column, left_diagonal, right_diagonal)
    
    return answer