n_k =  input().split(" ") 
n, k = int(n_k[0]), int(n_k[1])

title_company = [input() for _ in range(k)]

# description = []
# for _ in range(n):
#     s = input()
#     info = {int(s[0]):[int(s[1]), s[2]]}
#     description.append(info)
description = [{0:[1, 'a']}, {1:[2, 'a']}, {1:[2, 'b']}, {1:[1, 'b']}, {4:[2, 'a']}]


spisok = []
while len(description) > 0:
    elem = description.pop(0)
    sum = 0
    for i in description:
        comp = ''
        if elem < i:
            for j in description[i].values():
                sum += j[0]
                comp = j[1]
        spisok.append([sum, comp])

print(spisok)