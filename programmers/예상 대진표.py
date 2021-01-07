def solution(n,a,b):
    answer = 0
    if a > b:
        a, b = b, a
        
    left, right = 1, n
    while True:
        if left <= a <= (left+right)//2 and (left+right)//2 < b <= n:
            break
        else:
            if a > (left+right)//2:
                left = (left+right)//2+1
            else:
                right = (left+right)//2
    
    criteria = (right-left)+1
    while criteria > 1:
        criteria //= 2
        answer += 1

    return answer