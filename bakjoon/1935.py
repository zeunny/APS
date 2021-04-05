import sys
input = sys.stdin.readline

def operation(o, m, n):
  if o == '+':
    return m + n
  elif o == '-':
    return m - n
  elif o == '*':
    return m * n
  else: # /
    return m / n

N = int(input())
operand = input().strip()

stack = []
alpha_num = {}

unit = ord('A')
for _ in range(N):
  alpha_num[chr(unit)] = int(input())
  unit += 1

for o in operand:
  if o in '+-*/':
    n = stack.pop()
    m = stack.pop()
    stack.append(operation(o, m, n))
  else:
    stack.append(alpha_num[o])

print(f'{stack[0]:0.2f}')