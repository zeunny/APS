def solution(s):
    length = len(s)
    while length > 0:
        middle = length // 2
        for i in range(len(s)-length+1):
            for k in range(middle):
                if s[i+k] != s[i+length-k-1]:
                    break
            else:
                return length
        length -= 1