# # n_k = list(map(int, '52'))
# n_k = list(map(int, input().split()))
# print(n_k)


n_k =  input().split(" ") 
n, k = int(n_k[0]), int(n_k[1])


# title_company = ''
# for _ in range(k):
#     title_company += input()
# print(title_company)    
title_company = [input() for _ in range(k)]

# description = []
# for _ in range(n):
#     s = input()
#     info = {int(s[0]):[int(s[1]), s[2]]}
#     description.append(info)
description = [{0:[1, 'a']}, {1:[2, 'a']}, {1:[2, 'b']}, {1:[1, 'b']}, {4:[2, 'a']}]

for i in description[0].values():
    root = i 
print(root)
l1 = []
for i in range(1, n):
    if description[0] != description[i]:
        for j in description[i].values():
            elem = [root[0]+j[0], [root[1], j[1]]]
        l1.append(elem)
print(l1)
# minimum_amount_of_money = [0, '']
# for i in l1:
#     if i[0] > minimum_amount_of_money[0] and title_company in i[1]:
#         minimum_amount_of_money[0] = i[0]
#         minimum_amount_of_money[1] = i[1]
# if minimum_amount_of_money[1] == '':
#     print(-1)
# else:
#     print(minimum_amount_of_money[0])
