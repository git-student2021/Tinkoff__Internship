n_k =  input().split(" ") 
n, k = int(n_k[0]), int(n_k[1])


title_company = ''
for _ in range(k):
    title_company += input()

description = []
for _ in range(n):
    s = input().split(' ')
    info = {int(s[0]):[int(s[1]), s[2]]}
    description.append(info)

for i in description[0].values():
    root = i 

l1 = []
for i in range(1, n):
    if description[0] != description[i]:
        for i in description[i].values():
            elem = [root[0]+i[0], root[1]+i[1]]
        l1.append(elem)

minimum_amount_of_money = [0, '']
for i in l1:
    if i[0] > minimum_amount_of_money[0] and title_company in i[1]:
        minimum_amount_of_money[0] = i[0]
        minimum_amount_of_money[1] = i[1]
if minimum_amount_of_money[1] == '':
    print(-1)
else:
    print(minimum_amount_of_money[0])