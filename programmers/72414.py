def change_sec(time):
    hh, mm, ss = map(int,time.split(':'))
    return hh*3600 + mm*60 + ss

def solution(play_time, adv_time, logs):
    play_time_sec = change_sec(play_time)
    adv_time_sec = change_sec(adv_time)
    
    if play_time_sec == adv_time_sec:
        return '00:00:00'
    
    logs_start_sec, logs_end_sec = [], []
    for log in logs:
        s, e = log.split('-')
        logs_start_sec.append(change_sec(s))
        logs_end_sec.append(change_sec(e))
    
    total_time = [0]*(play_time_sec+1)
    
    for i in range(len(logs_start_sec)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1
    
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]
        
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]
    
    max_time, answer = total_time[adv_time_sec], 0
    for i in range(adv_time_sec+1, play_time_sec+1):
        if total_time[i] - total_time[i-adv_time_sec] > max_time:
            max_time = total_time[i] - total_time[i-adv_time_sec]
            answer = i - adv_time_sec + 1
    
    hh = answer // 3600
    answer %= 3600
    mm = answer // 60
    ss = answer % 60
    
    return f'{hh:02d}:{mm:02d}:{ss:02d}'