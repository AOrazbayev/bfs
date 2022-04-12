from queue import SimpleQueue

n, m, s, t = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

d = [float('inf')]*n
d[s] = 0
p = [None] * n
q = SimpleQueue()
q.put(s)
while not q.empty():
    u = q.get()
    for v in adj_list[u]:
        if d[v] == float('inf'):
            d[v] = d[u] + 1
            p[v] = u
            q.put(v)
        #elif v == s:

print(d)
path = []
cur = t
while cur is not None:
    path.append(cur)
    cur = p[cur]

print(*path[::-1])

