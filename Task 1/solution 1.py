logo = "TINKOFF"
num = int(input())
for _ in range(num):
    word = input()
    if len(word) == len(logo):
        if sorted(word) == sorted(logo):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


logo = "TINKOFF"
num = int(input())
for _ in range(num):
    word = input()
    if len(word) == len(logo):
        if sorted(word) == sorted(logo):
            print("Yes")
    else:
        print("No")