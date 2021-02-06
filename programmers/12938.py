def solution(n, s):
    answer = []
    
    while n > 1:
        q = s // n
        
        if q == 0:
            return [-1]
        
        s -= q    
        answer.append(q)
        n -= 1
        
    answer.append(s)
        
    return answer