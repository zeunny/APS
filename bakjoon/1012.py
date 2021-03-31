import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  answer = 0
  M, N, K = map(int,input().split())

  cabbages = [[0]*M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int,input().split())
    cabbages[Y][X] = 1

  directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
  for i in range(N):
    for j in range(M):
      if cabbages[i][j]:
        cabbages[i][j] = 0
        stack = [(i, j)]
        while stack:
          n, m = stack.pop()
          for y, x in directions:
            new_n = n + y
            new_m = m + x
            if 0 <= new_n < N and 0 <= new_m < M and cabbages[new_n][new_m]:
              cabbages[new_n][new_m] = 0
              stack.append((new_n, new_m))
        answer += 1

  print(answer)