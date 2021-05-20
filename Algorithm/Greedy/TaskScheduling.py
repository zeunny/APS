# 작업 스케줄링 문제 : 가장 적은 개수의 기계를 사용하여 작업 간의 충돌이 발생하지 않도록 모든 작업을 기계에 할당하는 문제

def TaskScheduling(T, n): # T: 이차원 배열 T[i][0] - 작업 i의 시작시간, T[i][1]: 작업 i의 완료 시간 / n: 작업의 개수
  T.sort()
  m = 0   # m : 모든 작업을 완료하는데 필요한 기계의 개수
  machine = []
  for i in range(n):
    for j, v in enumerate(machine):
      if v <= T[i][0]:
        machine[j] = T[i][1]
        break
    else:
      m += 1
      machine.append(T[i][1])

  return m

print(TaskScheduling([(0, 5), (6, 9), (4, 9), (2, 4), (0, 7), (9, 10), (7, 10), (5, 8)], 8))