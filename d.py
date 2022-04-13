from collections import deque


def bfs(s, t): 
    q = deque()
    q.append(s)
    p = [None] * Nx * Ny
    p[s] = -1
    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if p[v] is None:
                p[v] = u
                q.append(v)
            if v == t:
                path = [t]
                cur = u
                while cur != -1:
                    path.append(cur)
                    cur = p[cur]
                return path[::-1]
    return []


def strtoi(coord):
    y = ord(coord[0]) - ord('a')
    x = int(coord[1]) - 1
    return x * 8 + y


def itostr(r):
    x = r // 8
    y = r % 8
    return str(chr(ord('a') + y)) + str(x + 1)


Nx = 8
Ny = 8
adj_list = [set() for _ in range(Nx * Ny)]

for k in range(Nx * Ny):
    for i in [-2, -1, 1, 2]:
        for j in [-2, -1, 1, 2]:
            if abs(i) == abs(j):
                continue
            cur_x = k % Nx
            cur_y = k // Nx
            new_x = cur_x + i
            new_y = cur_y + j
            if (-1 < new_x < Nx) & (-1 < new_y < Ny):
                adj_list[k].add(new_x + new_y * Nx)

# for i, j in enumerate(adj_list):
#     for k in j:
#         print(i % Nx, i // Nx, k % Nx, k // Nx, i, k)

s = strtoi(input())
t = strtoi(input())

for i in bfs(s, t):
    print(itostr(i))
