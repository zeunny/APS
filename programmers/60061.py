import collections

def solution(n, build_frame):
    answer = []
    
    pillar = {} # 기둥
    beam = {} # 보
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if y == 0 or pillar.get((x, y-1)) or beam.get((x, y)) or beam.get((x-1, y)):
                    pillar[(x, y)] = 1
            else:
                if pillar.get((x, y-1)) or pillar.get((x+1, y-1)) or (beam.get((x-1, y)) and beam.get((x+1, y))):
                    beam[(x, y)] = 1
        else:
            if a == 0:
                if pillar.get((x, y+1)):
                    if not (beam.get((x, y+1)) or beam.get((x-1, y+1))):
                        continue
                if beam.get((x-1, y+1)):
                    if not (pillar.get((x-1, y)) or (beam.get((x-2, y+1)) and beam.get((x, y+1)))):
                        continue
                if beam.get((x, y+1)):
                    if not (pillar.get((x+1, y)) or (beam.get((x-1, y+1)) and beam.get((x+1, y+1)))):
                        continue
                del pillar[(x, y)]
            else:
                if pillar.get((x, y)):
                    if not (pillar.get((x, y-1)) or beam.get((x-1, y))):
                        continue
                if pillar.get((x+1, y)):
                    if not (pillar.get((x+1, y-1)) or beam.get((x+1, y))):
                        continue
                if beam.get((x-1, y)):
                    if not (pillar.get((x-1, y-1)) or pillar.get((x, y-1))):
                        continue
                if beam.get((x+1, y)):
                    if not (pillar.get((x+1, y-1)) or pillar.get((x+2, y-1))):
                        continue
                del beam[(x, y)]
                    
                
    for key, value in pillar.items():
        answer.append([key[0], key[1], 0])
        
    for key, value in beam.items():
        answer.append([key[0], key[1], 1])
        
    return sorted(answer)