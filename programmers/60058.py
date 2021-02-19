import collections

def check(p):
    # 올바른 괄호 문자열인지 확인
    cnt = 0
    for char in p:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
            # 올바른 괄호 문자열이 아닌 경우 break
            if cnt < 0:
                return False
    return True

def solution(p):
    if not p:
        return p
    
    if check(p):
        return p
    
    # 올바른 괄호 문자열이 아닌 경우 u, v로 분리하기
    bracket = collections.defaultdict(int)
    for i in range(len(p)):
        bracket[p[i]] += 1
        if bracket['('] == bracket[')']:
            break
    u = p[:i+1]
    v = p[i+1:]
    
    if check(u):
        return u + solution(v)
    else:
        temp = ''
        for char in u[1:-1]:
            if char == '(':
                temp += ')'
            else:
                temp += '('
        return '(' + solution(v) + ')' + temp