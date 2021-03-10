hanoi = [[[1,3]]]

def tower_of_hanoi(n):
    i = 0
    while i < n-1:
        prev = hanoi[-1]
        result = []
        for a, b in prev:
            if a == 2:
                a = 3
            elif a == 3:
                a = 2
            if b == 2:
                b = 3
            elif b == 3:
                b = 2
            result.append([a, b])
        result.append([1, 3])
        for a, b in prev:
            if a == 1:
                a = 2
            elif a == 2:
                a = 1
            if b == 1:
                b = 2
            elif b == 2:
                b = 1
            result.append([a, b])
        hanoi.append(result)
        i += 1

def solution(n):
    tower_of_hanoi(n)
    return hanoi[-1]