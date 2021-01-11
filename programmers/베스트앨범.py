import collections

def solution(genres, plays):
    answer = []
    play_times = collections.defaultdict(int)
    genre_hashmap = collections.defaultdict(list)
    
    for i in range(len(genres)):
        play_times[genres[i]] += plays[i]
        genre_hashmap[genres[i]].append((-plays[i], i))
        
    while play_times:
        for key, value in play_times.items():
            if value == max(play_times.values()):
                genre = key
                break
                
        play_list = sorted(genre_hashmap[genre])
        if len(play_list) > 1:
            answer += [play_list[0][1], play_list[1][1]]
        else:
            answer.append(play_list[0][1])
        del play_times[genre]
        
    return answer