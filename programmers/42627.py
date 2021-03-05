import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))
        if not heap:
            time += 1
            continue
        count += 1
        last = time
        term, start = heapq.heappop(heap)
        time += term
        answer += time - start
        
    return answer//len(jobs)