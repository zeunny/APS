import collections

def search_block(item):
    first_i = item[0][0]
    first_j = item[0][1]
    x = y = 0
    for i, j in item:
        x += i
        y += j
    x -= first_i*4
    y -= first_j*4
    
    z, w = item[0]
    if (x, y) == (3, 3) and item[0][0] != item[1][0]:
        return [(z,w+1), (z,w+2)]
    elif (x, y) == (5, -1):
        return [(z+1,w-1)]
    elif (x, y) == (5, 1):
        return [(z+1,w+1)]
    elif (x, y) == (3, -3):
        return [(z,w-2), (z,w-1)]
    elif (x, y) == (3, 0):
        return [(z,w-1), (z,w+1)]
    else:
        return False
        

def solution(board):
    answer = 0
    
    blocks = collections.defaultdict(list)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                blocks[board[i][j]].append((i, j))
    
    while True:
        flag = False
        delete_key = []
        for key, value in blocks.items():
            value.sort()
            searchs = search_block(value)
            if searchs:
                count = 0
                for k in searchs:
                    i = k[0]
                    while i >= 0:
                        if board[i][k[1]]:
                            break
                        i -= 1
                    else:
                        count += 1
                if count == len(searchs):
                    flag = True
                    answer += 1
                    for v in value:
                        board[v[0]][v[1]] = 0
                    delete_key.append(key)
        if not flag:
            return answer
        
        for key in delete_key:
            del blocks[key]