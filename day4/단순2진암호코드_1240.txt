import sys
sys.stdin = open('input.txt','r')
check_code = ['0001101',
             '0011001',
             '0010011',
             '0111101',
             '0100011',
             '0110001',
             '0101111',
             '0111011',
             '0110111',
             '0001011']


T = int(input().strip()) + 1

for test_case in range(1, T):
    N, M = map(int,input().split())
    input_list = [input() for _ in range(N)]
    data = "".join(input_list)
    end = data.rfind('1')
    start = end-55
    ans = [data[i:i+7] for i in range(start, end, 7)]
    ans2 = [check_code.index(ans[i]) for i in range(8)]
    chk = ((ans2[0]+ans2[2]+ans2[4]+ans2[6])*3 + (ans2[1]+ans2[3]+ans2[5]+ans2[7]))%10
    if chk:
        print('#%d 0'%test_case)
    else:
        print('#%d %d' % (test_case, sum(ans2)))