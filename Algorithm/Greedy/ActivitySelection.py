# 작업 선택 문제 : 하나의 기계만을 사용해서 충돌 없이 최대 개수의 작업을 기계에 할당하는 문제

def ActivitySelection(T, n):  # T: 이차원 배열 T[i][0] - 작업 i의 시작시간, T[i][1]: 작업 i의 완료 시간 / n: 작업의 개수
  T.sort(key=lambda x: x[1])
  m = 0
  machine = 0
  for i in range(n):
    if machine <= T[i][0]:
      machine = T[i][1]
      m += 1
    
  return m

print(ActivitySelection([(1, 3), (0, 4), (1, 6), (4, 6), (3, 8), (4, 8), (6, 9), (9, 10)], 8))