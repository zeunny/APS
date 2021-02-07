def solution(k, room_number):
    answer = []
    visited = {}
    
    for value in room_number:
        room = value
        
        if not visited.get(room):
            answer.append(room)
            visited[room] = room + 1   
            
        else:
            update = []
            while visited.get(room):
                update.append(room)
                room = visited[room]
                
            answer.append(room)
            
            for u in update:
                visited[u] = room + 1
            visited[room] = room + 1
            
    return answer