def solution(n, t, m, timetable):
    timetable = list(map(lambda x: int(x[:2])*60 + int(x[3:]), timetable))
    timetable.sort(reverse=True)
    
    boarding_time = 540
    while n > 0:
        count = m
        if n == 1:
            while timetable and timetable[-1] <= boarding_time and count > 1:
                timetable.pop()
                count -= 1   
                
            if timetable and timetable[-1] <= boarding_time:
                answer = timetable[-1] - 1
            else:
                answer = boarding_time
            
            return f'{answer // 60:02d}:{answer % 60:02d}'

        else:
            while timetable and timetable[-1] <= boarding_time and count > 0:
                timetable.pop()
                count -= 1
                
        boarding_time += t
        n -= 1