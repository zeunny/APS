import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
  command = input()
  if command.startswith('push'):
    stack.append(int(command.split()[-1]))
  elif command.startswith('pop'):
    print(stack.pop()) if stack else print(-1)
  elif command.startswith('size'):
    print(len(stack))
  elif command.startswith('empty'):
    print(0) if stack else print(1)
  else:
    print(stack[-1]) if stack else print(-1)