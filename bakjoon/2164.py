import collections

N = int(input())

queue = collections.deque(list(range(1, N+1)))

while len(queue) > 2:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[-1])