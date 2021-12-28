def solution(sizes):
    max_width = max_height = 0
    
    for width, height in sizes:
        basic = max(width, max_width) * max(height, max_height)
        change = max(height, max_width) * max(width, max_height)
        
        if basic < change:
            max_width = max(width, max_width)
            max_height = max(height, max_height)
        else:
            max_width = max(height, max_width)
            max_height = max(width, max_height)
    
    return max_width * max_height