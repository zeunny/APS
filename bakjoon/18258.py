import sys, collections

input = sys.stdin.readline

N = int(input())

queue = collections.deque([])
for _ in range(N):
  command = input().strip()
  if command.startswith('push'):
    queue.append(command.split()[-1])
  elif command.startswith('pop'):
    print(queue.popleft()) if queue else print(-1)
  elif command.startswith('size'):
    print(len(queue))
  elif command.startswith('empty'):
    print(0) if queue else print(1)
  elif command.startswith('front'):
    print(queue[0]) if queue else print(-1)
  else: # back
    print(queue[-1]) if queue else print(-1)