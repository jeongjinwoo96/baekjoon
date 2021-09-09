a = int(input())
b = []
for _ in range(a):
    b.append(list(map(int,input().split())))

for i in range(a):
    r = ((b[i][0]-b[i][3])**2 + (b[i][1]-b[i][4])**2)**(1/2)
    if r > b[i][2] + b[i][5] or r < abs(b[i][2]-b[i][5]):
        print(0)
    elif r == abs(b[i][2]-b[i][5]) or r == b[i][2]+b[i][5]:
        print(1)
    elif abs(b[i][2]-b[i][5]) < r and r < b[i][2]+b[i][5]:
        print(2)
    else:
        print(-1)
