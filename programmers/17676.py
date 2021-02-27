import collections

def solution(lines):
    treat = []
    first_time = 0
    for line in lines:
        date, time, T = line.split()
        time = time.split(':')
        time = list(map(float,time))
        time = time[2] + time[1]*60 + time[0]*60*60
    
        T = float(T[:-1])
        start_time = int(round(time - T + 0.001, 3)*1000)
        end_time = int(time*1000)
        
        for t in range(start_time-999, end_time+1):
            if t >= 0:
                treat.append(t)
        
    return collections.Counter(treat).most_common(1)[0][1]