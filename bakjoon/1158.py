N, K = map(int,input().split())

people = list(range(1, N+1))

mod, index = N, K

orders = []
while people:
  orders.append(people.pop((index-1)%mod))
  index = (index-1)%mod+K
  mod -= 1

print('<', end='')
print(*orders, sep=', ', end='')
print('>')