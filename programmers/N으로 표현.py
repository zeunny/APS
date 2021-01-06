def solution(N, number):
    if number == N:
        return 1
    number_list = [set() for _ in range(9)]
    number_list[1].add(N)

    for n in range(2, 9):
        number_list[n].add(int(str(N)*n))
        for k in range(1, n//2+1):
            for i in number_list[k]:
                for j in number_list[n-k]:
                    number_list[n].add(i+j)
                    number_list[n].add(i-j)
                    number_list[n].add(j-i)
                    number_list[n].add(i*j)
                    if j != 0:
                        number_list[n].add(i//j)
                    if i != 0:
                        number_list[n].add(j//i)
        if number in number_list[n]:
            return n
    
    return -1