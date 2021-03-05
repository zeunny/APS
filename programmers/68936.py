count_zero = count_one = 0

def compress(arr):
    global count_zero, count_one
    
    number = arr[0][0]
    flag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != number:
                flag = 1
                break
        if flag:
            break
    else:
        if number == 0:
            count_zero += 1
        else:
            count_one += 1
        return
    
    arr_list = []
    arr_list.append([[arr[i][j] for j in range(len(arr)//2)] for i in range(len(arr)//2)])
    arr_list.append([[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(len(arr)//2)])
    arr_list.append([[arr[i][j] for j in range(len(arr)//2)] for i in range(len(arr)//2, len(arr))])
    arr_list.append([[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(len(arr)//2, len(arr))])

    for k in range(4):
        compress(arr_list[k])
                
def solution(arr):
    compress(arr)
    return [count_zero, count_one]