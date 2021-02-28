import sys
from collections import deque

sys.setrecursionlimit(10**4)

pre_answer, post_answer = [], []

def arrange(nodeinfo):
    if len(nodeinfo) == 0:
        return
    
    nodeinfo.sort(key=lambda x: ([x[1], x[0]]), reverse=True)
    
    pre_answer.append(nodeinfo[0][2])
    
    child = [[], []]
    for x, y, index in nodeinfo:
        if y == nodeinfo[0][1]:
            continue
        if x < nodeinfo[0][0]:
            child[0].append((x, y, index))
        else:
            child[1].append((x, y, index))
    
    arrange(child[0])
    arrange(child[1])
    
    post_answer.append(nodeinfo[0][2])
    
def solution(nodeinfo):
    for index in range(len(nodeinfo)):
        nodeinfo[index].append(index+1)
        
    arrange(nodeinfo)
    
    return [pre_answer, post_answer]