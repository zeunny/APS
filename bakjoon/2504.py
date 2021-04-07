bracket = input()

stack, value = [], []
for item in bracket:
  if item in '([':
    stack.append(item)
    value.append(0)
    continue

  elif item == ')':
    if stack and stack[-1] == '(':
      stack.pop()
      if value[-1] == 0:
        value[-1] = 2
      else:
        temp = 0
        while value[-1] != 0:
          temp += value.pop()
        value[-1] = temp*2
      continue

  else: # item == ']'
    if stack and stack[-1] == '[':
      stack.pop()
      if value[-1] == 0:
        value[-1] = 3
      else:
        temp = 0
        while value[-1] != 0:
          temp += value.pop()
        value[-1] = temp*3
      continue

  print(0)
  break

else:
  if stack:
    print(0)
  else:
    print(sum(value))