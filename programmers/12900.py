def solution(n):
    tile = [0]*60001
    tile[1] = 1
    tile[2] = 2
    tile[3] = 3

    for i in range(4, n+1):
        tile[i] = (tile[i-2] + tile[i-1])%1000000007
    
    return tile[n]