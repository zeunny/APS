import sys

input = sys.stdin.readline

N = int(input())

solutions = list(map(int,input().strip().split()))

solutions.sort()
minV = 2000000000
value = []
left, right = 0, N-1

while left < right:
  ans = solutions[left] + solutions[right]

  if abs(ans) <= minV:
    minV = abs(ans)
    value = [solutions[left], solutions[right]]

  if ans < 0:
    left += 1
  else:
    right -= 1

value.sort()

print(value[0], value[-1])