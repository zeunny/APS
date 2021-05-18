def ChainedMatrix(n, d):   # n: 행렬의 개수, d: 행렬의 크기(배열)
  C = [[0]*(n+1) for _ in range(n+1)]   # C: n개의 행렬을 곱하는데 필요한 곱셈 횟수의 최소값
  P = [[0]*(n+1) for _ in range(n+1)]   # P: 최적의 곱셈 순서를 구할 수 있는 배열
  for i in range(1, n+1):
    C[i][i] = 0
  for s in range(1, n):
    for i in range(1, n-s+1):
      j = i+s
      minV = float('inf')
      for k in range(i, j):
        if C[i][k]+C[k+1][j]+d[i-1]*d[k]*d[j] < minV:
          minV = C[i][k]+C[k+1][j]+d[i-1]*d[k]*d[j]
          P[i][j] = k
      C[i][j] = minV
  return C[1][n]

print(ChainedMatrix(3, [3, 2, 4, 1]))