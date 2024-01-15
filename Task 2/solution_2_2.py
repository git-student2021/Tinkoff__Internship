t = 4

n = 2
ai = [1, 1]

# for i in ai:

cnt = ai.count(1)
if (0 in ai) or (max(ai) >= n) or (cnt != max(ai)):
    result = 'NO'
else:
    result = 'YES'

print(result)