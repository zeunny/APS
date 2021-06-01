N = int(input())
Array = list(map(int,input().split()))

M = int(input())
list_x = list(map(int,input().split()))

Array.sort()

def BinarySearch(Array, x):
  left, right = 0, len(Array)-1

  while left <= right:
    mid = (left+right)//2
    if Array[mid] == x:
      return 1

    if Array[mid] < x:
      left = mid+1
    else:
      right = mid-1
  return 0

for x in list_x:
    print(BinarySearch(Array, x))