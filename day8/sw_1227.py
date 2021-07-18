import sys

sys.stdin = open('../input.txt', 'r')
T = 10

n = int(input())
graph = [list(map(int, input())) for i in range(101)]
count = 0
