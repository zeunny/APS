def solution(cookie):
    answer = 0
    
    for m in range(len(cookie)):
        l, r = 0, len(cookie)-1
        first_son, second_son = sum(cookie[:m+1]), sum(cookie[m+1:])
        while l <= m < r:
            if first_son == second_son:
                if first_son > answer:
                    answer = first_son
                break
                
            if first_son > second_son:
                first_son -= cookie[l]
                l += 1
            else:
                second_son -= cookie[r]
                r -= 1
                
            if first_son < answer and second_son < answer:
                break
        
    return answer