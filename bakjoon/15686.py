N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]

house = []
chicken = []
street = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

CN = len(chicken)
combi = [0]*M; minV = 0xffffff
def solve(k,s):
    global minV
    if k == M:
        minS = 0
        for i in range(len(house)):
            minH = 0xfffff
            for j in range(M):
                if abs(house[i][0]-chicken[combi[j]][0]) + abs(house[i][1]-chicken[combi[j]][1]) < minH:
                    minH = abs(house[i][0]-chicken[combi[j]][0]) + abs(house[i][1]-chicken[combi[j]][1])
            minS += minH
            if minS > minV:
                return
        if minS < minV:
            minV = minS
    else:
        for i in range(s, CN-M+k+1):
            combi[k] = i
            solve(k+1,i+1)

solve(0,0)
print(minV)