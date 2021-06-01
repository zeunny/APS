def MergeSort(Array):
  if len(Array) == 1:
    return Array

  mid = len(Array)//2
  left_array = MergeSort(Array[:mid])
  right_array = MergeSort(Array[mid:])

  return merge(left_array, right_array)

def merge(A, B):
  i = j = 0
  new_array = []

  while i < len(A) and j < len(B):
    if A[i] < B[j]:
      new_array.append(A[i])
      i += 1
    else:
      new_array.append(B[j])
      j += 1
  
  new_array += A[i:]
  new_array += B[j:]

  return new_array

array = []

N = int(input())

for _ in range(N):
    array.append(int(input()))
    
for x in MergeSort(array):
    print(x)