from collections import deque

m, n = map(int, input().split())
sy, sx = map(int, input().split())
ty, tx = map(int, input().split())

s = sx+sy*n
t = tx+ty*n
adj_list = [set() for _ in range(n*m)]
current = input()
next = input()
for y in range(m):
    for x in range(n):
        if x != n - 1:
            if (current[x] != 'X') & (current[x + 1] != 'X'):
                adj_list[x + y * n].add(x + 1 + y * n)
                adj_list[x + 1 + y * n].add(x + y * n)
        if y != m - 1:
            if (current[x] != 'X') & (next[x] != 'X'):
                adj_list[x + y * n].add(x + (y + 1) * n)
                adj_list[x + (y + 1) * n].add(x + y * n)
    if y < m - 2:
        current = next
        next = input()

d = [float('inf')] * n * m
d[s] = 0
q = deque()
q.append(s)
p = [None] * n * m
p[s] = -1
while q:
    u = q.popleft()
    for v in adj_list[u]:
        if d[v] == float('inf'):
            d[v] = d[u] + 1
            p[v] = u
            q.append(v)

# for i,j in enumerate(adj_list):
#     for k in j:
#         print(i//n, i%n, k//n, k%n)

if d[t] == float('inf'):
    print('INF')
else:
    print(d[t])