import sys

input = sys.stdin.readline

dp = [0, 0, 1, 7, 4, 2, 0, 8, 10, 18]
min_dp = [0]*101

def calculate():
  for i in range(10):
    min_dp[i] = dp[i]
  
  min_dp[6] = 6

  for i in range(10, 101):
    min_dp[i] = min_dp[i-2]*10 + dp[2]

    for j in range(3,8):
      min_dp[i] = min(min_dp[i], min_dp[i-j]*10+dp[j])

calculate()
T = int(input())

for _ in range(T):
  n = int(input())
  q = n//2
  if n%2:
    max_value = '7' + '1'*(q-1)
  else:
    max_value = '1'*q
  
  print(min_dp[n], max_value)