import collections

visited = collections.defaultdict(list)

def check(w1, w2):
    if w2 in visited[w1]:
        return False
    if w1 in visited[w2]:
        return False
    
    visited[w1].append(w2)
    visited[w2].append(w1)
    return True

def solution(board):
    N = len(board)
    robot = [[(0,0),(0,1)],0,0] # 가로방향 0, 세로방향 1 / robot[-1]은 시간
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # 상, 하, 좌, 우
    
    visited[(0,0)].append((0,1))
    visited[(0,1)].append((0,0))
    
    q = collections.deque([robot])
    
    while q:
        r, shape, time = q.popleft()
        
        if r[0] == (N-1,N-1) or r[1] == (N-1,N-1):
            return time
        
        r.sort()
        
        for i, d in enumerate(directions):
            flag = False
            for y, x in r:
                if y+d[0] < 0 or y+d[0] > N-1:
                    flag = True
                    break
                if x+d[1] < 0 or x+d[1] > N-1:
                    flag = True
                    break
                if board[y+d[0]][x+d[1]] == 1:
                    flag = True
                    break
            if flag:
                continue
                
            wheel1, wheel2 = r
            new_wheel1 = (wheel1[0]+d[0], wheel1[1]+d[1])
            new_wheel2 = (wheel2[0]+d[0], wheel2[1]+d[1])
            if check(new_wheel1, new_wheel2):
                q.append([[new_wheel1, new_wheel2], shape, time+1])
                
            if shape == 0:
                if i == 0:
                    new_wheel1 = wheel1
                    new_wheel2 = (wheel2[0]-1, wheel2[1]-1)
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 1, time+1])
                    
                    new_wheel1 = (wheel1[0]-1, wheel1[1]+1)
                    new_wheel2 = wheel2
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 1, time+1])
                if i == 1:
                    new_wheel1 = wheel1
                    new_wheel2 = (wheel2[0]+1, wheel2[1]-1)
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 1, time+1])
                    
                    new_wheel1 = (wheel1[0]+1, wheel1[1]+1)
                    new_wheel2 = wheel2
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 1, time+1])
                        
            if shape == 1:
                if i == 2:
                    new_wheel1 = (wheel1[0]+1, wheel1[1]-1)
                    new_wheel2 = wheel2
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 0, time+1])
                    
                    new_wheel1 = wheel1
                    new_wheel2 = (wheel2[0]-1, wheel2[1]-1)
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 0, time+1])
                if i == 3:
                    new_wheel1 = (wheel1[0]+1, wheel1[1]+1)
                    new_wheel2 = wheel2
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 0, time+1])
                    
                    new_wheel1 = wheel1
                    new_wheel2 = (wheel2[0]-1, wheel2[1]+1)
                    if check(new_wheel1, new_wheel2):
                        q.append([[new_wheel1, new_wheel2], 0, time+1])