n_m_q =  input().split(" ")   
n, m, q = int(n_m_q[0]), int(n_m_q[1]), int(n_m_q[2])

l = input().split(' ')
amount = []
for i in range(n):
    amount.append(int(l[i]))

friends = [input().split(' ') for _ in range(m)]

for i in range(q):
    event = input().split(' ')
    l1 = [ int(i) for i in event[1:] ]
    if  '?' in event:
        print(amount[l1[0]-1])
    elif '+' in event:
        for j in friends:
            if l1[0] == int(j[0]):
                amount[int(j[1])-1] = amount[int(j[1])-1] + l1[1]
            elif l1[0] == int(j[1]):
                amount[int(j[0])-1] = amount[int(j[0])-1] + l1[1]