def solution(food_times, k):
    length_ft = len(food_times)
    sort_ft = [0] + sorted(food_times)
    for i in range(1,len(food_times)+1):
        remove_time = (sort_ft[i]-sort_ft[i-1])*length_ft
        if k - remove_time < 0:
            break
        k -= remove_time
        length_ft -= 1
    else:
        return -1

    value = sort_ft[i]
    cnt = k % (len(food_times)-i+1)
    for i, food_time in enumerate(food_times):
        if food_time >= value:
            if cnt == 0:
                return i+1
            cnt -= 1