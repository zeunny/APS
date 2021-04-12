import sys, collections

input = sys.stdin.readline

N, M = map(int,input().split())

string = collections.defaultdict(int)
for _ in range(N):
  string[input()] = 1

cnt = 0
for _ in range(M):
  if string[input()] == 1:
    cnt += 1

print(cnt)