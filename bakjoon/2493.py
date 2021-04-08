N = int(input())
tops = list(map(int,input().split()))

laser = [0]*N
stack = []
for i in range(N-1, -1, -1):
  top = tops[i]
  while stack and top > stack[-1][0]:
    laser[stack[-1][1]] = i+1
    stack.pop()
  stack.append((top, i))

print(*laser)