import heapq

def solution(a):
    answer = 0
    left_heap, right_heap = [], []
    left_value, right_value = a[0], a[-1]
    for i in range(1, len(a)//2):
        if a[i] < left_value:
            answer += 1
            left_value = a[i]
            while left_heap and left_heap[0][1] > min(left_value, right_value):
                heapq.heappop(left_heap)
        elif a[i] < right_value:
            heapq.heappush(left_heap, (-a[i], a[i]))

        if a[-1-i] < right_value:
            answer += 1
            right_value = a[-1-i]
            while right_heap and right_heap[0][1] > min(left_value, right_value):
                heapq.heappop(right_heap)
        elif a[-1-i] < left_value:
            heapq.heappush(right_heap, (-a[-1-i], a[-1-i]))
    
    if len(a)%2 and a[len(a)//2] < max(left_value, right_value):
        answer += 1
    
    while left_heap and left_heap[0][1] > max(left_value, right_value):
        heapq.heappop(left_heap)
    while right_heap and right_heap[0][1] > max(left_value, right_value):
        heapq.heappop(right_heap)

    return answer + len(left_heap) + len(right_heap) + 2