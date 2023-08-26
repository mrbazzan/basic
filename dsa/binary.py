import queue


q = queue.Queue()
q.put('1')

for _ in range(5):
    x = q.get()
    q.put(x + '0')
    q.put(x + '1')
    print(x)
