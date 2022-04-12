from queue import Queue

n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

d = [float('inf')]*n
d[0] = 0
p = [None] * n
q = Queue()
q.put(0)
while not q.empty():
    u = q.get()
    for v in adj_list[u]:
        if d[v] == float('inf'):
            d[v] = d[u] + 1
            p[v] = u
            q.put(v)
        #elif v == s:

for i in d:
    print(i)

