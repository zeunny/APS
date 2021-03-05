import heapq

def change_heap(heap):
    new_heap = []
    for h in heap:
        heapq.heappush(new_heap, -h)
    return new_heap

def solution(operations):
    max_heap, min_heap = [], []
    for operation in operations:
        w, n = operation.split()
        if w == 'I':
            heapq.heappush(max_heap, -int(n))
            heapq.heappush(min_heap, int(n))
        else:
            if max_heap:
                if n == '1':
                    heapq.heappop(max_heap)
                    min_heap = change_heap(max_heap)
                else:
                    heapq.heappop(min_heap)
                    max_heap = change_heap(min_heap)
    
    if max_heap:
        return [-heapq.heappop(max_heap),heapq.heappop(min_heap)]
    else:
        return [0,0]