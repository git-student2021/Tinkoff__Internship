n = int(input())

for i in range(n):
    dev = int(input())
    hands = input().split(" ")
    counter = int(hands[0])
    for h in hands[1:]:
        counter += int(h)
        counter -= 2
    if counter < 0:
        print("No")
    else:
        print("Yes")