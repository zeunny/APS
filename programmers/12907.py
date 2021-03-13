def solution(n, money):
    money.sort()
    table = [[0]*(n+1) for _ in range(len(money))]
    
    for j in range(0, n+1, money[0]):
        table[0][j] = 1
    
    for i in range(1,len(money)):
        for j in range(n+1):
            table[i][j] = (table[i-1][j] + table[i][j-money[i]]) % 1000000007
        
    return table[-1][-1]