from collections import deque

def solve(conyPosition, brownPosition): 
  time = 0 
  visit = [[0]*2 for _ in range(200001)] 
  q = deque() 
  q.append((brownPosition, 0)) 
  
  while 1: 
    conyPosition += time 
    
    if conyPosition > 200000: 
      return -1 
    if visit[conyPosition][time%2]:
      return time
      
    for i in range(0, len(q)): 
      current = q.popleft() 
      currentPosition = current[0] 
      newTime = (current[1]+1)%2 
      
      newPosition = currentPosition - 1 
      if newPosition >= 0 and not visit[newPosition][newTime]: 
        visit[newPosition][newTime] = True 
        q.append((newPosition, newTime)) 
        
      newPosition = currentPosition + 1 
      if newPosition < 200001 and not visit[newPosition][newTime]:
        visit[newPosition][newTime] = True 
        q.append((newPosition, newTime)) 
        
      newPosition = currentPosition * 2 
      if newPosition < 200001 and not visit[newPosition][newTime]: 
        visit[newPosition][newTime] = True 
        q.append((newPosition, newTime)) 
    time+=1

print(solve(3, 3))