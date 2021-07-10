a = 1 # 00000001
b = 2 # 00000010

print('& :',a&b)
print('| :',a|b)
print('^ :',a^b)

ch = 97
key = 100

print("ch : %c" % ch)
ch = ch ^ key
print("ch : %c" % ch)
ch = ch ^ key
print("ch : %c" % ch)
