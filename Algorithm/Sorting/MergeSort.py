# def merge(A, B):
#   A_pointer, B_pointer = 0, 0
#   new_array = []
#   while A_pointer < len(A) and B_pointer < len(B):
#     if A[A_pointer] < B[B_pointer]:
#       new_array.append(A[A_pointer])
#       A_pointer += 1
#     else:
#       new_array.append(B[B_pointer])
#       B_pointer += 1
  
#   while A_pointer < len(A):
#     new_array.append(A[A_pointer])
#     A_pointer += 1
#   while B_pointer < len(B):
#     new_array.append(B[B_pointer])
#     B_pointer += 1

#   return new_array

# def MergeSort(Array):
#   if (len(Array) > 1):
#     mid = len(Array)//2
#     A = MergeSort(Array[:mid])
#     B = MergeSort(Array[mid:])
#     return merge(A, B)
#   else:
#     return Array


# 2. 손코딩

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


print(MergeSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))