import re

def solution(files):
    answer = []
    
    p = re.compile('([^0-9]+)(\d{1,5})')
    orders = []
    for i, file in enumerate(files):
        order = list(re.findall(p, file)[0])
        order.append(i)
        orders.append(order)
        
    orders.sort(key=lambda x: (x[0].lower(), int(x[1]), x[2]))
    
    for order in orders:
        answer.append(files[order[2]])
    
    return answer