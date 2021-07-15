v, E = map(int, input().split())
q = [[] for _ in range(v + 1)]

print(q)
stc = []
visited = [True] * (V + 1)
for i in range(E):
    s, e = map(int, input().split())
    q[s].append(e)
    q[e].append(e)


stc.append(1)
visited[1] = False
print('dfs : [', end=' ')
while  stc:
    u = stc.pop()
    print(u, end=' ')
    for i in q[u]:
        if visited[i]:
            stc.append(i)
            visited[i] = False