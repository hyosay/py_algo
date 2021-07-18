import sys
sys.stdin = open('../input.txt', 'r')

def priority(c):
    if c == '*' or c == '/':
        return 1
    elif c == '+' or c == '-':
        return 2
    else:
        return 3

for test_case in range(1, 11):
    n = int(input())
    data = input()
    postStr = []
    stk = []
    for i in data:
        if i < '0':
            if i == '(':
                stk.append(i)
            elif i == ')':
                peek = stk[-1]
                while peek != '(':
                    postStr.append(stk.pop())
                    peek = stk[-1]
                stk.pop()
            else:
                peek = stk[-1]
                while stk and priority(i) >= priority(peek):
                    postStr.append(stk.pop())
                    peek = stk[-1]
                stk.append(i)
        else:
            postStr.append(i)

    while stk:
        postStr.append(stk.pop())


    for i in postStr:
        if i >= '0':
            stk.append(int(i))
        elif i == '*':
            a = stk.pop()
            b = stk.pop()
            stk.append(b * a)
        elif i == '/':
            a = stk.pop()
            b = stk.pop()
            stk.append(b / a)
        elif i == '+':
            a = stk.pop()
            b = stk.pop()
            stk.append(b + a)
        else:
            a = stk.pop()
            b = stk.pop()
            stk.append(b - a)
    print('#%d %d' % (test_case, stk.pop()))