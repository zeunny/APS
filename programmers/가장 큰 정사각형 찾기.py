def solution(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or j == 0:
                continue
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1

    maxV = 0
    for b in board:
        if max(b) > maxV:
            maxV = max(b)
            
    return maxV * maxV