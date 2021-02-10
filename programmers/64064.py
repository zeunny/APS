def solution(user_id, banned_id):
    answer = 0
    banned = []
    user = [False]*len(user_id)


    def search(k,n):
        nonlocal answer, temp, user, check
        if k == n:
            for t in temp:
                if set(t) == check:
                    break
            else:
                temp.append(list(check))
                answer += 1
        else:
            for i in range(len(banned[k])):
                if not user[banned[k][i]]:
                    user[banned[k][i]] = True
                    check.add(banned[k][i])
                    search(k+1,n)
                    user[banned[k][i]] = False
                    check.remove(banned[k][i])


    for i in range(len(banned_id)):
        banlen = len(banned_id[i])
        temp = []
        for j in range(len(user_id)):
            if banlen == len(user_id[j]):
                for k in range(banlen):
                    if banned_id[i][k] != user_id[j][k] and banned_id[i][k] != '*':
                        break
                else:
                    temp.append(j)
        banned.append(temp)

    temp = []
    check = set()
    search(0,len(banned))

    return answer
