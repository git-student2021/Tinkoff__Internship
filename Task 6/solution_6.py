# n_q = list(map(int, '63'))
# n_q = list(map(int, input()))

n_q =  input().split(" ") #list(map(int, input().split())) 
n, q = int(n_q[0]), int(n_q[1])
f = input().split(' ')
a = []
for i in range(n):
    a.append(int(f[i]))

print(a)
# a = [2, 4, 6, 8, 10, 12] # [ int(i) for i in input() ]

# '?2530'
# '+236'
# '?2532'

for i in range(q):
    qw = input().split(' ')
    if '?' in qw:
        l1 = [ int(i) for i in qw[1:] ]
        l2 = a[l1[0]-1:l1[1]]
        l3 = max(l2)
        ind = a.index(l3) + 1
        print(min(l3, l1[2]*ind+l1[-1] ))
    elif '+' in qw:
        l1 = [ int(i) for i in qw[1:] ]
        l2 = a[l1[0]-1:l1[1]]
        for j in range(n):
            if l1[0]-1 <= j <= l1[1]-1:
                a[j] = a[j] + l1[-1]