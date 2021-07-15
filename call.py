import sys
sys.stdin = open('day8/input.txt', 'r')

T = int(input())


key = list(map(int, input().split()))
print(key)
arr = list(map(int, input().split()))
print(arr)
#0<=K < N