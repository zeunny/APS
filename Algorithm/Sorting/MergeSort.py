def merge(A, B):
  A_pointer, B_pointer = 0, 0
  new_array = []
  while A_pointer < len(A) and B_pointer < len(B):
    if A[A_pointer] < B[B_pointer]:
      new_array.append(A[A_pointer])
      A_pointer += 1
    else:
      new_array.append(B[B_pointer])
      B_pointer += 1
  
  while A_pointer < len(A):
    new_array.append(A[A_pointer])
    A_pointer += 1
  while B_pointer < len(B):
    new_array.append(B[B_pointer])
    B_pointer += 1

  return new_array

def MergeSort(Array):
  if (len(Array) > 1):
    mid = len(Array)//2
    A = MergeSort(Array[:mid])
    B = MergeSort(Array[mid:])
    return merge(A, B)
  else:
    return Array

print(MergeSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))