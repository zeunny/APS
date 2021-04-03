import sys

input = sys.stdin.readline

n = int(input())

wine = []
max_value = [0]*n

for _ in range(n):
  wine.append(int(input()))

if len(wine) < 3:
  print(sum(wine))
else:
  max_value[0] = wine[0]
  max_value[1] = sum(wine[:2])
  max_value[2] = max(max_value[1], max_value[0]+wine[2], wine[1]+wine[2])
  for i in range(3, n):
    max_value[i] = max(max_value[i-1], max_value[i-2]+wine[i], max_value[i-3]+wine[i-1]+wine[i])
  print(max_value[-1])