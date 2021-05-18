def Scale(n, w, M):   # n: 추의 개수, w: 추의 무게 배열, M: 물체의 무게
  S = [[0]*(M+1) for _ in range(n+1)]

  for j in range(M+1):
    S[0][j] = 0

  for i in range(n+1):
    S[i][0] = 1

  for i in range(1, n+1):
    for j in range(1, M+1):
      if j-w[i-1] < 0:
        S[i][j] = S[i-1][j]
      else:
        S[i][j] = max(S[i-1][j], S[i-1][j-w[i-1]])
  
  return S[n][M]

print(Scale(4, [7, 8, 5, 3], 13))