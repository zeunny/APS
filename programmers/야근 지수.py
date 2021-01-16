def solution(n, works):
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    
    left, right = 0, len(works)-1
    while left <= right:
        middle = (left + right) // 2
        count = 0
        for i in range(middle):
            count += works[i] - works[middle]
        if count <= n:
            works = ([works[middle]] * middle) + works[middle:]
            n -= count
            left = middle + 1
        else:
            right = middle - 1
        if n == 0:
            return sum([i**2 for i in works])

    if middle == 0:
        works[0] -= n
    else:
        i = 0
        while n > 0:
            if works[i] <= 0 or i == left:
                i = 0
                continue
            works[i] -= 1
            n -= 1
            i += 1
                
    return sum([i**2 for i in works])