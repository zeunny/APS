def Knapsack(p, w, M, n):   # p[i], w[i]: 물체 i의 이익과 무게 / n, M: 물체의 개수와 배낭의 용량
  p_w = [(p[i]/w[i], i) for i in range(n)]
  p_w.sort(reverse=True)

  # X: 배낭에 들어간 물체 i의 비율
  X = [0]*n
  for i in range(n):
    if p_w[i][0] * w[p_w[i][1]] <= M:
      X[i] = 1
      M -= w[p_w[i][1]]
    else:
      break
  
  if i < n:
    X[i] = M // w[p_w[i][1]]

  return X

'''
물체를 쪼갤 수 없는 형태의 배낭 문제는 욕심쟁이 방법을 적용할 수 없다.
'''