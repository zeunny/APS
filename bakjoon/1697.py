import collections

N, K = map(int,input().split())

queue = collections.deque([N])

time = 0
visited = collections.defaultdict(int)
visited[N] = 1

while queue:
  time += 1

  for _ in range(len(queue)):
    n = queue.popleft()

    if n == K:
      print(time-1)
      queue.clear()
      break

    if 0 <= n-1 and not visited[n-1]:
      queue.append(n-1)
      visited[n-1] = 1
    if n+1 <= 100000 and not visited[n+1]:
      queue.append(n+1)
      visited[n+1] = 1
    if 2*n <= 100000 and not visited[2*n]:
      queue.append(2*n)
      visited[2*n] = 1