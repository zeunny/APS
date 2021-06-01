# 1.
def BinarySearch(Array, left, right, x):
  if left > right:
    return -1
  
  mid = (left + right) // 2
  if Array[mid] == x:
    return mid

  if Array[mid] < x:
    BinarySearch(Array, left, mid-1, x)
  else:
    BinarySearch(Array, mid+1, right, x)


# 2.
def BinarySearch(Array, x):
  left, right = 0, len(Array)-1
  while left <= right:
    mid = (left+right)//2

    if Array[mid] == x:
      return mid

    if Array[mid] < x:
      right = mid-1
    else:
      left = mid+1
  
  return -1

# 3. 손코딩
def BinarySearch(Array, x):
  Array.sort()
  left, right = 0, len(Array)-1

  while left <= right:
    mid = (left+right)//2
    if Array[mid] == x:
      return mid

    if Array[mid] < x:
      left = mid+1
    else:
      right = mid-1