import sys

input = sys.stdin.readline

N = int(input())
balloons = list(map(int,input().split()))

index, balloon, cnt = 0, 0, 0
answer = []
while cnt < N:

  while balloon != 0:
    if balloon > 0:
      index = (index+1)%N
      if balloons[index] != 0:
        balloon -= 1
    else:
      index = (index-1+N)%N
      if balloons[index] != 0:
        balloon += 1

  answer.append(index+1)
  balloon, balloons[index] = balloons[index], 0

  cnt += 1
  
print(*answer)