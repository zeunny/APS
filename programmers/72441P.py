import itertools, collections

def solution(orders, course):
    answer = []
    sample_menu = collections.defaultdict(int)
    
    for order in orders:
        for n in range(2, len(order)+1):
            for i in itertools.combinations(order, n):
                sample_menu[''.join(sorted(list(i)))] += 1
    
    checked = [0]*11
    maxV = [2]*11
    menus = []
    for c in course:
        checked[c] = 1
        
    for key, value in sample_menu.items():
        if checked[len(key)]:
            if maxV[len(key)] <= value:
                menus.append((key, value))
                maxV[len(key)] = value
                
    for menu, cnt in menus:
        if maxV[len(menu)] == cnt:
            answer.append(menu)
    
    return sorted(answer)