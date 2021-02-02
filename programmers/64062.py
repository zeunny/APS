def solution(stones, k):
    answer = 0
    
    left, right = 0, 200000000
    while left <= right:
        middle = (left+right) // 2
        not_cross = 0
        for stone in stones:
            if stone <= middle:
                not_cross += 1
            else:
                not_cross = 0
            
            if not_cross >= k:
                right = middle - 1
                answer = middle
                break
        else:
            left = middle + 1
            
    return answer