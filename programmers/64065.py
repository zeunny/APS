def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    for i in range(len(s)):
        s[i] = list(map(int,s[i].split(',')))
    s.sort(key = len)
    
    for element in s:
        for i in range(len(element)):
            if element[i] in answer:
                pass
            else:
                answer.append(element[i])
                break     
                
    return answer