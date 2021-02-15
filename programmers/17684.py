def solution(msg):
    answer = []
    
    num = 65
    LZW = {}
    while num < 91:
        LZW[chr(num)] = num-64
        num += 1
    
    num, i = 27, 0
    while i < len(msg):
        w = msg[i]
        while i+1 < len(msg) and w in LZW:
            i += 1
            w += msg[i]
        if w in LZW:
            answer.append(LZW[w])
            break
        answer.append(LZW[w[:-1]])
        LZW[w] = num
        num += 1
        
    return answer