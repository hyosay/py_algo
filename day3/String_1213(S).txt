import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')
for test_case in range(1, 11):
    input()
    key = input()
    s = input()
    print('#%d %d'%(test_case,s.count(key)))
