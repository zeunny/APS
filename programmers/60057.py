def solution(s):
    minV = len(s)
    for k in range(1,len(s)//2+1):
        temp = ''; cnt = 0; tempV = ''
        for i in range(0,len(s),k):
            if temp == s[i:i+k]:
                cnt += 1
            else:
                if cnt > 1:
                    tempV += str(cnt)
                tempV += temp
                temp = s[i:i+k]
                cnt = 1
                if len(tempV) > minV:
                    break
        else:
            if cnt > 1:
                tempV += str(cnt)
            tempV += temp
            temp = s[i:i+k]
            cnt = 1
            
        if len(tempV) < minV:
            minV = len(tempV)

    return minV