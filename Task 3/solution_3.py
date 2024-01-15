n_m =  input().split(" ") #list(map(int, input().split())) 
n, m = int(n_m[0]), int(n_m[1])
l = input().split(' ')
l1 = []
for i in range(n):
    l1.append(int(l[i]))

# l1 = [5, 4, 1]
# l1 = [1, 2, 3]
l1.sort(reverse=True)

l = []
for i in l1:
    ind = l1.index(i)
    srez = l1[:ind]+l1[(ind+1):]
    num1 = i - 1
    for j in srez:
        if num1 < j:
            num1 = num1
        else:
            num1 -= j
    l.append(num1)

max_sum = m - sum(l1)
if max_sum > max(l):
    print(max_sum)
else:
    print(max(l))