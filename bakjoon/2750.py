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

def BubbleSort(array):
  N = len(array)
  for i in range(N-1):
    flag = False
    for j in range(N-1-i):
      if array[j] > array[j+1]:
        flag = True
        array[j], array[j+1] = array[j+1], array[j]
    if not flag:
      break
  return array

def SelectionSort(array):
  N = len(array)
  for i in range(N-1):
    min_index = i
    for j in range(i+1, N):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  return array

def InsertionSort(array):
  N = len(array)
  for i in range(1, N):
    value = array[i]
    for j in range(i-1, -1, -1):
      if array[j] > value:
        array[j+1] = array[j]
      else:
        array[j+1] = value
        break
    else:
      array[j] = value
  return array

array = []

N = int(input())

for _ in range(N):
    array.append(int(input()))
    
for x in InsertionSort(array):
    print(x)