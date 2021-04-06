bracket = input()

stack = []
answer = 0
for index, value in enumerate(bracket):
  if value == '(':
    stack.append(value)
  else:
    stack.pop()
    if bracket[index-1] == '(':
      answer += len(stack)
    else:
      answer += 1

print(answer)