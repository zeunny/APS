import sys

input = sys.stdin.readline

N, M = map(int,input().split())

poketmons_num = {}
poketmons_name = {}
for i in range(1,N+1):
  poketmon = input().strip()
  poketmons_num[i] = poketmon
  poketmons_name[poketmon] = i

for _ in range(M):
  problem = input().strip()
  if problem.isdigit():
    print(poketmons_num[int(problem)])
  else:
    print(poketmons_name[problem])