def EditDistance(s1, s2, insert, delete, change):   # s1: 원래 문자, s2: 바꿀 문자, ins: 삽입 비용, del: 삭제 비용, chg: 변경 비용
  E = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
  for i in range(len(s1)+1):
    E[i][0] = i
  for j in range(len(s2)+1):
    E[0][j] = j
  
  for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
      if s1[i-1] == s2[j-1]:
        E[i][j] = min(E[i-1][j]+delete, E[i][j-1]+insert, E[i-1][j-1])
      else:
        E[i][j] = min(E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+change)

  return E[len(s1)-1][len(s2)-1]

print(EditDistance('SNOWY', 'SUNNY', 1, 1, 2))