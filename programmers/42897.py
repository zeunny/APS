def solution(money):
    answer = 0
    
    if len(money) == 3:
        return max(money)
    
    if len(money) == 4:
        return max(money[0]+money[2], money[1]+money[3])
    
    remove_first = money[1:]
    remove_last = money[:-1]
    
    remove_first[2] += remove_first[0]
    remove_last[2] += remove_last[0]
    for i in range(3, len(remove_first)):
        remove_first[i] += max(remove_first[i-2], remove_first[i-3])
        remove_last[i] += max(remove_last[i-2], remove_last[i-3])
    
    answer = max(remove_first[-1], remove_first[-2], remove_last[-1], remove_last[-2])
    
    return answer