import itertools, collections

def solution(relation):
    answer = 0
    checked = []
    
    num_list = list(range(len(relation[0])))
    for i in range(1,len(relation)+1):
        if len(num_list) < i:
            break
        
        for numbers in itertools.combinations(num_list, i):
            components = []
            for rel in relation:
                component = []
                for number in numbers:
                    component.append(rel[number])
                components.append(tuple(component))
            most = collections.Counter(components).most_common(1)

            if most[0][1] == 1:
                flag = True
                for check in checked:
                    for c in check:
                        if c not in list(numbers):
                            break
                    else:
                        flag = False
                if flag:
                    answer += 1
                    checked.append(list(numbers))
        
    return answer