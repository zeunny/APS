expression = input().strip()

stack = []
orders = {'+': 2, '-': 2, '*': 1, '/': 1, '(': 3}

answer = ''
for value in expression:
  if value in '+-*/':
    while stack and orders[value] >= orders[stack[-1]]:
      answer += stack.pop()
    stack.append(value)
  elif value == '(':
    stack.append(value)
  elif value == ')':
    while stack and stack[-1] != '(':
      answer += stack.pop()
    stack.pop()
  else:
    answer += value
  
while stack:
  answer += stack.pop()

print(answer)