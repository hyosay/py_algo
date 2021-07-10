a = [[1, 2], [4, 5], [6, 4], [2, 1],[9, 6], [4, 1]]
b = sorted(a, key=lambda x: (x[1], x[0]))
print(b)