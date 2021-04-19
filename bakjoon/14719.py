H, W = map(int,input().split())

blocks = list(map(int,input().split()))
total_max_value = max(blocks)
left_max_value = blocks[0]

stack = []

rains = 0
for index in range(1,W):
  if blocks[index] < left_max_value and blocks[index] < total_max_value:
    rains += min(left_max_value, total_max_value) - blocks[index]
  elif index != W-1 and blocks[index] == total_max_value:
    left_max_value = total_max_value
    total_max_value = max(blocks[index+1:])
  elif blocks[index] > left_max_value:
    left_max_value = blocks[index]

print(rains)