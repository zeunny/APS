def solution(m, n, puddles):
    road = [[0]*m for _ in range(n)]
    road[0][0] = 1
    for puddle in puddles:
        x, y = puddle
        road[y-1][x-1] = -1
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0):
                continue
            if road[i][j] == -1:
                road[i][j] = 0
                continue
            if i-1 >= 0:
                road[i][j] += road[i-1][j]
            if j-1 >= 0:
                road[i][j] += road[i][j-1]
            road[i][j] %= 1000000007
    return road[n-1][m-1]