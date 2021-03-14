def solution(n, stations, w):
    answer = 0
    
    stations.append(n+w+1)
    
    answer += (stations[0]-w-1) // (2*w+1)
    if (stations[0]-w-1) % (2*w+1):
        answer += 1
    
    for index in range(1,len(stations)):
        count = (stations[index]-w) - (stations[index-1]+w) - 1
        if count != 0:
            answer += count // (2*w+1)
            if count % (2*w+1):
                answer += 1

    return answer