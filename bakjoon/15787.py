import sys

input = sys.stdin.readline

N, M = map(int,input().split())

train = [[0]*20 for _ in range(N)]

for _ in range(M):
  orders = list(map(int,input().split()))
  if orders[0] == 1:
    train[orders[1]-1][orders[2]-1] = 1
  elif orders[0] == 2:
    train[orders[1]-1][orders[2]-1] = 0
  elif orders[0] == 3:
    train[orders[1]-1] = [0] + train[orders[1]-1][:-1]
  else: # orders[0] == 4
    train[orders[1]-1] = train[orders[1]-1][1:] + [0]

cross = set()
for i in range(N):
  cross.add(''.join(map(str,train[i])))

print(len(cross))