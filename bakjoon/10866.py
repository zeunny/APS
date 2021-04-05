import sys, collections

input = sys.stdin.readline

N = int(input())
answer = []
deque = collections.deque([])
for _ in range(N):
  command = input()
  if command.startswith('push_front'):
    deque.appendleft(command.split()[-1])
  elif command.startswith('push_back'):
    deque.append(command.split()[-1])
  elif command.startswith('pop_front'):
    answer.append(deque.popleft()) if deque else answer.append(-1)
  elif command.startswith('pop_back'):
    answer.append(deque.pop()) if deque else answer.append(-1)
  elif command.startswith('size'):
    answer.append(len(deque))
  elif command.startswith('empty'):
    answer.append(0) if deque else answer.append(1)
  elif command.startswith('front'):
    answer.append(deque[0]) if deque else answer.append(-1)
  else: # back
    answer.append(deque[-1]) if deque else answer.append(-1)

print('\n'.join(map(str, answer)))