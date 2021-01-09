def solution(s):
    answer = [0, 0]
    while s != "1":
        count_one = s.count('1')
        answer[1] += len(s) - count_one
        s = bin(count_one)[2:]
        answer[0] += 1
            
    return answer