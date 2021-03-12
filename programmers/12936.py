def solution(n, k):
    if n == 1:
        return [1]
    
    line = list(range(1,n+1))
    
    result = []
    k -= 1
    while n > 0:
        number = n-1
        division = 1
        while number > 0:
            division *= number
            number -= 1
        result.append(line[k//division])
        del line[k//division]
        k = k%division
        n -= 1
    
    return result