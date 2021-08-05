def solution(s):
    answer = 0
    
    len_s = len(s)
    left_bracket = {'(', '{', '['}
    right_bracket_dict = {')': '(', '}': '{', ']': '['}
    
    index = 0
    while index < len_s:
        stack = []
        cnt = 0
        while cnt < len_s:
            if s[(index+cnt)%len_s] in left_bracket:
                stack.append(s[(index+cnt)%len(s)])
            elif stack and right_bracket_dict[s[(index+cnt)%len_s]] == stack[-1]:
                stack.pop()
            else:
                break
            cnt += 1
        else:
            if len(stack) == 0:
                answer += 1
        index += 1
    
    return answer