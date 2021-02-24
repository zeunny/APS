def rotate90(key, M):
    new_key = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[M-1-j][i]
    return new_key
            
def rotate180(key, M):
    new_key = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[M-1-i][M-1-j]
    return new_key
            
def rotate270(key, M):
    new_key = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[j][M-1-i]
    return new_key

def solution(key, lock):
    M = len(key)
    N = len(lock)
    new_lock = [[0]*(2*M+N-2) for _ in range(2*M+N-2)]
    for i in range(M-1,M-1+N):
        for j in range(M-1,M-1+N):
            new_lock[i][j] = lock[i-M+1][j-M+1]
    
    lock = new_lock
    
    key90 = rotate90(key, M)
    key180 = rotate180(key, M)
    key270 = rotate270(key, M)
    
    for m in range(M+N-1):
        for n in range(M+N-1):
            chk = chk90 = chk180 = chk270 = True
            for i in range(m, m+M):
                for j in range(n, n+M):
                    if M-1 <= i < M-1+N and M-1 <= j < M-1+N:
                        if chk and lock[i][j]^key[i-m][j-n] == 0:
                            chk = False
                        if chk90 and lock[i][j]^key90[i-m][j-n] == 0:
                            chk90 = False
                        if chk180 and lock[i][j]^key180[i-m][j-n] == 0:
                            chk180 = False
                        if chk270 and lock[i][j]^key270[i-m][j-n] == 0:
                            chk270 = False
                    if not (chk or chk90 or chk180 or chk270):
                        break
                if not (chk or chk90 or chk180 or chk270):
                    break
            else:
                flag = False
                for w in range(M-1,M-1+N):
                    for v in range(M-1,M-1+N):
                        if not (m <= w < m+M and n <= v < n+M):
                            if lock[w][v] == 0:
                                flag = True
                                break
                    if flag:
                        break
                else:
                    return True
    
    return False