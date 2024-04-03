a, b, c = int(input()), int(input()), int(input())
N = 3

list = [a,b,c]
for i in range(N-1):
    for j in range(N-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)