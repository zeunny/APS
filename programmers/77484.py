def solution(lottos, win_nums):
    answer = []
    zero_cnt, right_cnt = 0, 0
    
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        elif lotto in win_nums:
            right_cnt += 1
            
    answer.append(7-(right_cnt+zero_cnt) if 7-(right_cnt+zero_cnt) < 6 else 6)
    answer.append(7-right_cnt if 7-right_cnt < 6 else 6)
    
    return answer