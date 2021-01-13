def solution(routes):
    ENTER, EXIT, N = 0, 1, len(routes)
    routes = sorted(routes, key = lambda x:x[1])

    check = [False] * N
    camera, count = -30000, 0
    for i in range(N):
        if check[i]:
            continue
        count +=1
        camera = routes[i][EXIT]
        for i in range(i, N):
            if routes[i][ENTER] <= camera and camera <= routes[i][EXIT]:
                check[i] = True
                
    return count