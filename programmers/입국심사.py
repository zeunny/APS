def solution(n, times):
    times.sort()
    answer = 0
    left, right = 1, times[0]*n
    
    while left <= right:
        middle = (left + right) // 2
        
        count = 0
        for time in times:
            if middle // time == 0:
                break
            count += middle // time

        if count >= n:
            answer = middle
            right = middle - 1
        else:
            left = middle + 1
        
    return answer