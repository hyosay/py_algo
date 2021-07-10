'''input_list = ['123456789']

maxN = 9
for i in range(1):
    for j in range(maxN):
        for k in range(j):
            print(input_list[i][k:maxN-j+k])
        print('-' * 10)'''

a = [1, 2, 3]
b = [4, 5]
a.extend(b)
a.append(b)
a.pop(2)
print(a)