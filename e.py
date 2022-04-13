from collections import deque

m, n = map(int, input().split())

adj_list = [set() for _ in range(n * m)]
lmap = []

for _ in range(m):
    lmap.append(list(map(int, input().split())))

def my_func(p):
    x = p%n
    y = p//n
    r = l = d = u = 1
    while r < n + 1:
        if x + r == n:
            if r > 1:
                adj_list[x + y * n].add(x + r - 1 + y * n)
            break
        if lmap[y][x + r] == 2:
            adj_list[x + y * n].add(x + r + y * n)
            break
        if lmap[y][x + r] == 1:
            if r > 1:
                adj_list[x + y * n].add(x + r - 1 + y * n)
            break
        r += 1
    while l < n + 1:
        if x - l == -1:
            if l > 1:
                adj_list[x + y * n].add(x - l + 1 + y * n)
            break
        if lmap[y][x - l] == 2:
            adj_list[x + y * n].add(x - l + y * n)
            break
        if lmap[y][x - l] == 1:
            if l > 1:
                adj_list[x + y * n].add(x - l + 1 + y * n)
            break
        l += 1
    while d < m + 1:
        if y + d == m:
            if d > 1:
                adj_list[x + y * n].add(x + (y + d - 1) * n)
            break
        if lmap[y + d][x] == 2:
            adj_list[x + y * n].add(x + (y + d) * n)
            break
        if lmap[y + d][x] == 1:
            if d > 1:
                adj_list[x + y * n].add(x + (y + d - 1) * n)
            break
        d += 1
    while u < m + 1:
        if y - u == -1:
            if u > 1:
                adj_list[x + y * n].add(x + (y - u + 1) * n)
            break
        if lmap[y - u][x] == 2:
            adj_list[x + y * n].add(x + (y - u) * n)
            break
        if lmap[y - u][x] == 1:
            if u > 1:
                adj_list[x + y * n].add(x + (y - u + 1) * n)
            break
        u += 1
#print(adj_list)

d = [float('inf')] * n * m
d[0] = 0
q = deque()
q.append(0)
p = [None] * n * m
p[0] = -1
while q:
    u = q.popleft()
    my_func(u)
    for v in adj_list[u]:
        if d[v] == float('inf'):
            d[v] = d[u] + 1
            p[v] = u
            q.append(v)
        if lmap[v//n][v%n] == 2:
            print(d[v])
            exit()

# for i,j in enumerate(adj_list):
#     for k in j:
#         print(i//n, i%n, k//n, k%n)


