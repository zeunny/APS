import sys

input = sys.stdin.readline

N = int(input())

for n in range(N):
  current_list = list(map(int,input().split()))

  if n > 0:
    for i in range(n+1):
      current_list[i] += max(before_list[i], before_list[i+1])

  before_list = [0] + current_list + [0]

print(max(current_list))