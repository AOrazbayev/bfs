from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    p = [None] * n
    p[s] = -1
    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if p[v] is None:
                p[v] = u
                q.append(v)
            elif v == s:
                cycle = []
                cur = u
                while cur != -1:
                    cycle.append(cur)
                    cur = p[cur]
                return cycle[::-1]
    return []


n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)

c_len = float('inf')
shortest = []

for s in range(n):
    cycle = bfs(s)
    if cycle and len(cycle)<c_len:
        shortest = cycle
        c_len = len(cycle)

if c_len == float('inf'):
    print("NO CYCLES")
else:
    print(*shortest)