def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    
    sticker1 = sticker[:-1]
    sticker2 = sticker[1:]
    
    sticker1[2] += sticker1[0]
    sticker2[2] += sticker2[0]
    for index in range(3, len(sticker1)):
        sticker1[index] += max(sticker1[index-2], sticker1[index-3])
        sticker2[index] += max(sticker2[index-2], sticker2[index-3])

    return max(sticker1[-1], sticker1[-2], sticker2[-1], sticker2[-2])