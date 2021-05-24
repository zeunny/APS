def SelectionSort(A):
  n = len(A)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if A[j] < A[min_index]:
        min_index = j
    A[i], A[min_index] = A[min_index], A[i]
  return A

print(SelectionSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))