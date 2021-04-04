import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  stack = []
  VPS = input().rstrip('\n')
  for v in VPS:
    if v == '(':
      stack.append(v)
    else:
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  else:
    if stack:
      print('NO')
    else:
      print('YES')