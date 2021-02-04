import heapq

def solution(board):
    min_price = 0xffffff
    directions = {(0, 1, 'j'), (1, 0, 'i'), (0, -1, 'j'), (-1, 0, 'i')}
    visited = [[0]*len(board) for _ in range(len(board))]
    visited[0][0] = 2
    
    heap = []
    
    if not board[0][1]:
        visited[0][1] = 2
        heapq.heappush(heap, (100, 0, 1, 'j'))
    
    if not board[1][0]:
        visited[1][0] = 2
        heapq.heappush(heap, (100, 1, 0, 'i'))
        
    while heap:
        price, i, j, load = heapq.heappop(heap)
        visited[i][j] += 1
        
        if price >= min_price:
            return min_price
        
        if i == len(board)-1 and j == len(board)-1:
            
            if price < min_price:
                min_price = price
            
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < len(board) and 0 <= new_j < len(board):
                if not board[new_i][new_j] and visited[new_i][new_j] < 2:
                    if load == direction[2]:
                        heapq.heappush(heap, (price+100, new_i, new_j, direction[2]))
                    else:
                        heapq.heappush(heap, (price+600, new_i, new_j, direction[2]))
        
    
    return min_price