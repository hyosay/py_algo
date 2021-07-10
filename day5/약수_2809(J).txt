import sys
sys.stdin = open("input.txt", "r")

import math

n = int(input())
sq = int(math.sqrt(n))+1
ans={1,n}
for i in range(2,sq):
    if(n%i == 0):
       ans.add(i)
       ans.add(int(n/i))
tt = sorted(ans)

for i in tt:
    print(i,end=" ")
print()
'''
ans=[1,n]
for i in range(2,sq):
    if(n%i == 0):
       ans.append(i)
       if n/i != i:
           ans.append(int(n/i))
#ans.append(n)
ans.sort()
for i in ans:
    print(i,end=" ")
print();
'''