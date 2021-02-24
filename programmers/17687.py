def solution(n, t, m, p):
    answer = '0'
    
    i = 1
    while len(answer) < t*m:
        temp = ''
        num = i
        while num > 0:
            if n > 10:
                if num%n >= 10:
                    temp += chr(num%n+55)
                else:
                    temp += str(num%n)
            else:
                temp += str(num%n)
            num //= n
        answer += temp[::-1]
        i += 1
    
    tube = ''
    order = p-1
    while len(tube) < t:
        tube += answer[order]
        order += m
    
    return tube