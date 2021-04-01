import sys

input = sys.stdin.readline

N = int(input())

before_R = 0
for _ in range(N):
  R, G, B = map(int, input().split())

  if before_R:
    R += min(before_G, before_B)
    G += min(before_R, before_B)
    B += min(before_R, before_G)

  before_R, before_G, before_B = R, G, B

print(min(R, G, B))