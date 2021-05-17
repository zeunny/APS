def Partition(Array):
  left, right = 1, len(Array)-1

  while left < right:
    while left < len(Array) and Array[left] < Array[0]:
      left += 1
    while right > 0 and Array[right] > Array[0]:
      right -= 1
    
    if left < right:
      Array[left], Array[right] = Array[right], Array[left]
    else:
      Array[0], Array[right] = Array[right], Array[0]

  return right

def QuickSort(Array):
  if len(Array) > 1:
    pivot = Partition(Array)
    return QuickSort(Array[:pivot]) + [Array[pivot]] + QuickSort(Array[pivot+1:])
  else:
    return Array

print(QuickSort([30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85]))