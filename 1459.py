x,y,w,s = map(int, input().split())
m = min(x,y)
M = max(x,y)
if x==0 or y==0:
    if M % 2 ==0:
        if w < s:
            print(M * w)
        else:
            print(M * s)
    else:
        if (M-1)*s + w < M*w:
            print((M-1)*s + w)
        else:
            print(M*w)

elif w*2 < s:
    print((x+y)*w)
    
elif (x+y - 2 * m) % 2 == 0:
    if w<s:
        print(m * s + (x+y-2 * m) * w)
    else:
        print(m * s + (x+y-2 * m) * s)
        
else:
    if s < w:
        print(m*s + (x+y-2*m-1)*s + w)
    else:
        print(m*s + (x+y-2*m)*w)
