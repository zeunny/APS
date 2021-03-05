def solution(n):
    jump = [0]*2001
    jump[0] = 1
    jump[1] = 1
    
    for i in range(2, n+1):
        jump[i] = (jump[i-2] + jump[i-1])%1234567
        
    return jump[n]