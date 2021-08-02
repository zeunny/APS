directions = [(0,1), (1,0), (0,-1), (-1,0)]

def rotate(matrix, y1, x1, y2, x2):
    min_value = save = matrix[y1][x1]
    
    index, i, j = 0, y1, x1
    while index < 4:
        ni = i + directions[index][0]
        nj = j + directions[index][1]
        
        if y1 <= ni <= y2 and x1 <= nj <= x2:
            matrix[ni][nj], save = save, matrix[ni][nj]
            min_value = min(min_value, matrix[ni][nj])
            i, j = ni, nj
        else:
            index += 1
            
    return matrix, min_value
    
def solution(rows, columns, queries):
    answer = []
    min_value = 0
    
    matrix = [[j for j in range(i, i+columns)] for i in range(1, rows*columns, columns)]
    
    for y1, x1, y2, x2 in queries:
        matrix, min_value = rotate(matrix, y1-1, x1-1, y2-1, x2-1)
        answer.append(min_value)
    
    return answer