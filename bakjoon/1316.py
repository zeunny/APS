import sys, collections

input = sys.stdin.readline

N = int(input())

answer = 0
for _ in range(N):
  stack = [x for x in input()]
  words = collections.defaultdict(int)

  while stack:
    w = stack.pop()
    while stack and stack[-1] == w:
      stack.pop()

    if words[ord(w)]:
      break
    else:
      words[ord(w)] = 1
  else:
    answer += 1

print(answer)