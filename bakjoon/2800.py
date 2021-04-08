import collections

expression = input()

answer = set()

def find(n, k, value, right_cnt, left_cnt=1, remove=[0]):
  if k == n:
    if value != expression:
      answer.add(value)
    return

  if expression[k] == '(':
    find(n, k+1, value, right_cnt, left_cnt+1, remove+[0])

    remove[-1] += 1
    find(n, k+1, value+expression[k], right_cnt, left_cnt+1, remove)
  elif expression[k] == ')':
    if remove[-1] == 0:
      find(n, k+1, value, right_cnt-1, left_cnt, remove[:-1])
    else:
      remove[-1] -= 1
      find(n, k+1, value+expression[k], right_cnt-1, left_cnt, remove)
  else:
    find(n, k+1, value+expression[k], right_cnt, left_cnt, remove)

find(len(expression), 0, '', expression.count(')'))

print(*sorted(list(answer)), sep='\n')