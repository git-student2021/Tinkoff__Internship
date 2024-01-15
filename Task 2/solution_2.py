def can_establish_contact(N, ai):
    groups = [[i] for i in range(N)] #создаем группы с одним разработчиком
    ai.sort
    print(ai)

    for i in range(N):
        if ai[i] == 0:
            continue
        for j in range(i+1, i+ai[i]-1):
            if j >= N or ai[j] == 0:
                return 'NO'
            groups[i].extend(groups[j]) #объединяем группы
            ai[j] -= 1                  #уменьшаем порог социальности
    return 'YES'

t = int(input())

for _ in range(t):
    N = int(input())
    ai = list(map(int, input().split())) #считываем пороги социальности

    result = can_establish_contact(N, ai)
    print(result)
