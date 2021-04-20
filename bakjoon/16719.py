import collections

words = list(map(lambda x: ord(x), input()))
W = len(words)

answer, cnt = ['']*len(words), 0
min_value, min_index = ord('Z')+1, -1
visited = collections.defaultdict(int)
while cnt < W:
  for i in range(min_index+1, len(words)):
    if words[i] < min_value and not visited[i]:
      min_value = words[i]
      min_index = i

  if not visited[min_index]:
    visited[min_index] = 1
    answer[min_index] = chr(words[min_index])
    print(''.join(answer))
    min_value = ord('Z')+1
    cnt += 1
  else:
    for i in range(len(words)-1, -1, -1):
      if visited[i] and i+1 < len(words) and not visited[i+1]:
        min_index = i
        break
    else:
      words = words[:words.index(min(words))]
      min_value, min_index = ord('Z')+1, -1