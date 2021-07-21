def solution(numbers):
    answer = []
    for number in numbers:
        binary_number = list(bin(number)[2:])
        
        for i in range(len(binary_number)-1, -1, -1):
            if binary_number[i] == '0':
                binary_number[i] = '1'
                if i+1 < len(binary_number):
                    binary_number[i+1] = '0'
                break
        else:
            binary_number = ['1', '0'] + binary_number[1:]
        
        binary_number = '0b' + ''.join(binary_number)
        
        answer.append(int(binary_number, 2))
    
    return answer