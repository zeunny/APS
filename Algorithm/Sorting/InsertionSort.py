def InsertionSort(A):
  n = len(A)
  for i in range(1, n):
    value = A[i]
    j = i
    while j > 0 and A[j-1] > value:
      A[j] = A[j-1]
      j -= 1
    A[j] = value
  return A

print(InsertionSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))