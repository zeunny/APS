def search_examinees(place):
    answer = []
    
    N = len(place)
    M = len(place[0])
    
    for i in range(N):
        for j in range(M):
            if place[i][j] == 'P':
                answer.append((i, j))
    
    return answer

def is_empty(place, r, c):
    if 0 <= r < 5 and 0 <= c < 5 and place[r][c] == 'O':
        return True
    return False

directions = {
    (-2, 0): [(-1, 0)],
    (0, -2): [(0, -1)],
    (-1, -1): [(-1, 0), (0, -1)],
    (2, 0): [(1, 0)],
    (0, 2): [(0, 1)],
    (1, 1): [(1, 0), (0, 1)],
    (-1, 1): [(-1, 0), (0, 1)],
    (1, -1): [(1, 0), (0, -1)]
}

def solution(places):
    answer = []
    
    for place in places:
        flag = 1
        
        examinees = search_examinees(place)
        len_examinees = len(examinees)
        examinees.sort()

        for standard_index in range(len_examinees-1):
            for comparison_index in range(standard_index+1, len_examinees):
                r1, c1 = examinees[standard_index]
                r2, c2 = examinees[comparison_index]
                
                taxicab_geometry = abs(r1-r2) + abs(c1-c2)

                if taxicab_geometry > 2:
                    continue

                if taxicab_geometry == 1:
                    flag = 0
                    break
                    
                distance = (r2-r1, c2-c1)

                for d_row, d_column in directions[distance]:
                    new_row = r1 + d_row
                    new_column = c1 + d_column

                    if is_empty(place, new_row, new_column):
                        flag = 0
                        break

                if not flag:
                    break
                
            if not flag:
                break
        
        answer.append(flag)
                
    return answer