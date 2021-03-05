def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    directions = {(1,0), (0,1), (1,1)}
    
    while True:
        remove_blocks = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 'X':
                    continue
                for x, y in directions:
                    if board[i+y][j+x] != board[i][j]:
                        break
                else:
                    remove_blocks.add((j, i))
                    for x, y in directions:
                        remove_blocks.add((j+x, i+y))
        
        if len(remove_blocks) == 0:
            return answer

        answer += len(remove_blocks)
        
        for j, i in remove_blocks:
            board[i][j] = 'X'
        
        for j in range(n):
            for i in range(m-1, 0, -1):
                if board[i][j] == 'X':
                    y = 1
                    while i-y > -1:
                        if board[i-y][j] != 'X':
                            board[i][j], board[i-y][j] = board[i-y][j], 'X'
                            break
                        y += 1
                    else:
                        break