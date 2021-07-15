'''
import heapq as hq

pq = []
hq.heappush(pq, 3)
hq.heappush(pq, 1)
hq.heappush(pq, 7)
hq.heappush(pq, 6)

print(pq)

print(hq.heappop(pq))
print(pq)
print(hq.heappop(pq))
print(pq)
print(hq.heappop(pq))
print(pq)
print(hq.heappop(pq))
print(pq)
'''

heap = [0]*11
top = 0

def user_print():
    print('[', end=' ')
    for i in range(1, top+1):
        print(heap[i], end=' ')
    print(']')

def push(d):
    global top
    top += 1
    heap[top] = d
    idx = top
    while True:
        if idx == 1 or heap[idx] > heap[idx//2]:
            break

        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx = idx//2

def pop():
    global top
    val = heap[1]
    heap[1] = heap[top]
    top -= 1

    idx = 1

    while True:
        next = idx * 2

        if next < top and heap[next] > heap[next+1]:
            next += 1

        if next > top or heap[idx] < heap[next]:
            break

        heap[idx], heap[next] = heap[next], heap[idx]
        idx = next

    return val

user_print()
push(4)
user_print()
push(3)
user_print()
push(2)
user_print()

print(pop())
user_print()
print(pop())
user_print()
print(pop())
user_print()

