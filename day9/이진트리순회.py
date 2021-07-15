from collections import deque
src = [0,'a', 'b', 'c','d','e','f','g','h','i','j',0,0,0,0,0,0,0,0,0,0,0]
leftC = [0,2,4,6,8,10,0,0,0,0,0]
rightC = [0,3,5,7,9,0,0,0,0,0,0]
def bfs(start):
    que = deque()
    que.append(start)

    print('bfs : [', end='')
    while que:
        u = que.popleft()
        print(src[u], end=' ')
        if src[u*2] != 0:
            que.append(u*2)
        if src[u*2+1] != 0:
            que.append(u*2+1)
    print(']')

def preOrder1(root):
    if src[root] == 0:
        return
    print(src[root], end=' ')
    preOrder1(root * 2)
    preOrder1(root * 2 + 1)

def preOrder2(root):
    if src[root] != 0:
        print(src[root], end=' ')
        preOrder2(root * 2)
        preOrder2(root * 2 + 1)

def preOrder3(root):
    if root != 0:
        print(src[root], end=' ')
        preOrder3(leftC[root])
        preOrder3(rightC[root])

def inOrder(root):
    if src[root] != 0:
        inOrder(root * 2)
        print(src[root], end=' ')
        inOrder(root * 2 + 1)

def postOrder(root):
    if src[root] != 0:
        postOrder(root * 2)
        postOrder(root * 2 + 1)
        print(src[root], end=' ')


bfs(1)
print('pre1 : [', end='')
preOrder1(1)
print(']')
print('pre2 : [', end='')
preOrder2(1)
print(']')
print('pre3 : [', end='')
preOrder3(1)
print(']')
print('in : [', end='')
inOrder(1)
print(']')
print('post : [', end='')
postOrder(1)
print(']')