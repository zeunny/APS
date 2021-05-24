def BubbleSort(A):   # A: 배열
  n = len(A)
  for i in range(n):
    for j in range(n-1-i):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]
  return A

print(BubbleSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))