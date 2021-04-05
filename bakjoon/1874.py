import sys

input = sys.stdin.readline

n = int(input())

criteria = 1
stack = []
operation = []
for _ in range(n):
  num = int(input())

  if num > criteria:
    while num >= criteria:
      stack.append(criteria)
      operation.append('+')
      criteria += 1
    else:
      stack.pop()
      operation.append('-')
  elif num < criteria:
    if stack and num == stack[-1]:
      stack.pop()
      operation.append('-')
    else:
      print('NO')
      break
  else:
    operation.append('+')
    operation.append('-')
    criteria += 1
else:
  print('\n'.join(operation))