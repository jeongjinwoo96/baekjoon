from collections import deque

n = int(input())
q = deque([-1,0,1])
idx = 3

for i in range(n):
    idx_plus = 0
    for _ in range(idx):
        a = q.popleft()
        if a == -1:
            q.append(0)
            q.append(1)
            idx_plus += 2
        elif a == 0:
            q.append(-1)
            q.append(0)
            q.append(1)
            idx_plus += 3
        else:
            q.append(-1)
            q.append(0)
            idx_plus += 2

    idx = idx_plus

print(len(q) % 9901)
