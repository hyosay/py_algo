data = ['a', 'b', 'c', 'd']

n = 4
for i in range((1<<n)):
    print("{", end="")
    for j in range(n):
        if i & (1 << j):
            print(data[j], end=' ')
    print('}')
