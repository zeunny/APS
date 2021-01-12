def change(m):
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')
    return m

def music_time(start, end):
    hour = (int(end[:2]) - int(start[:2])) * 60
    minute = (int(end[3:]) - int(start[3:]))
    return hour + minute

def music(time, music):
    quotient = time // len(music)
    reminder = time % len(music)
    return music * quotient + music[:reminder]

def solution(m, musicinfos):
    answer = []
    m = change(m)
    musicinfos = [musicinfo.split(',') for musicinfo in musicinfos]
    for musicinfo in musicinfos:
        musicinfo[3] = change(musicinfo[3])
        play_time = music_time(musicinfo[0], musicinfo[1])
        play_music = music(play_time, musicinfo[3])
        if m in play_music:
            answer.append((musicinfo[2], len(play_music)))
    answer.sort(key=lambda x: -x[1])
    return answer[0][0] if answer else '(None)'