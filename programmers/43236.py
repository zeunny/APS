def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    
    gaps = [rocks[0]]
    for i in range(1,len(rocks)):
        gaps.append(rocks[i]-rocks[i-1])
    gaps.append(distance-rocks[len(rocks)-1])

    left, right = 1, distance

    while left <= right:
        middle = (left + right) // 2
        count, diff = 0, 0
        min_value = float('inf')
        for gap in gaps:
            if gap + diff <= middle:
                count += 1
                diff += gap
            else:
                if gap + diff < min_value:
                    min_value = gap + diff
                diff = 0
        if count > n:
            right = middle - 1
        else:
            left = middle + 1
            answer = min_value

    return answer