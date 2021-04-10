import sys

input = sys.stdin.readline

N = int(input())

calendar = [0]*366
for _ in range(N):
  S, E = map(int,input().split())

  for n in range(S, E+1):
    calendar[n] += 1

i = 0
answer = 0
while i < 366:
  count, schedule = 0, 0
  while i < 366 and calendar[i] > 0:
    count += 1
    schedule = max(schedule, calendar[i])
    i += 1
  else:
    answer += count*schedule
    i += 1

print(answer)