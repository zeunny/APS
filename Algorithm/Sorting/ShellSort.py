def ShellSort(A):
  n = len(A)
  D = n//2
  while D > 0:
    for i in range(D, n):
      value = A[i]
      j = i
      while j > 0 and A[j-D] > value:
        A[j] = A[j-D]
        j -= D
      A[j] = value
    D //= 2
  return A

print(ShellSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))