import sys, collections

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N, M = map(int,input().split())
  importances = list(map(int,input().split()))

  queue = collections.deque([])
  for i in range(N):
    queue.append((importances[i], i))

  count = 1
  max_value = max(queue, key=lambda x: x[0])[0]
  while queue:
    importance, index = queue.popleft()

    if importance == max_value:
      if index == M:
        print(count)
        break
      count += 1
      max_value = max(queue, key=lambda x: x[0])[0]
    else:
      queue.append((importance, index))