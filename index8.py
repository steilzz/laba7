listFirst = [1, 2, 3, 4]
listSecond = []

n = len(listFirst) 
for i in range(n):
    for j in range(i+1, n):
        listSecond.append(listFirst[i] + listFirst[j])

print(listSecond)