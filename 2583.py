from collections import deque
m,n,k = map(int,input().split())
idx = [[0] * n for _ in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for p in range(x1,x2):
        for q in range(y1,y2):
            idx[q][p] = 1

cnt = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
for i in range(m):
    for j in range(n):
        if idx[i][j] != 1:
            count = 1
            idx[i][j] = 1
            q.append([i,j])
            while q:
                point = q.popleft()
                for k in range(4):
                    new_y = point[0]+dy[k]
                    new_x = point[1]+dx[k]
                    if 0<=new_y<m and 0<=new_x<n and idx[new_y][new_x] ==0:
                        idx[new_y][new_x] = 1
                        count += 1
                        q.append([new_y,new_x])
            cnt.append(count)
            
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i,end = ' ')
