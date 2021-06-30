def common_mesure_count(num):
    cnt = 0
    
    for n in range(1, num+1):
        if num % n == 0:
            cnt += 1
            
    return cnt

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if common_mesure_count(num) % 2:
            answer -= num
        else:
            answer += num
    
    return answer