t = 4

n = 4
ai = [1, 1, 2, 2]

groups = [[i] for i in range(n)]
ai.sort

for i in range(n):
    if ai[i] == 0:
        continue



    for j in range(i+1, i+ai[i]+1):
        if j >= n or ai[j] == 0:
            print('NO')
#             break
#         groups[i].extend(groups[j]) #объединяем группы
#         ai[j] -= 1                  #уменьшаем порог социальности
# print('YES')





# print(ai)