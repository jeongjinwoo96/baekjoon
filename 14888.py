N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = []

def dfs(add, sub, mul, div, val, idx):
    
    if idx == len(A):
        answer.append(val)
        return
    if add >= 1:
        dfs(add-1, sub, mul, div, val+A[idx], idx+1)
    if sub >= 1:
        dfs(add, sub-1, mul, div, val-A[idx], idx+1)
    if mul >= 1:
        dfs(add, sub, mul-1, div, val*A[idx], idx+1)
    if div >= 1:
        dfs(add, sub, mul, div-1, int(val/A[idx]), idx+1)
    
dfs(B[0],B[1],B[2],B[3],A[0],1)

print(max(answer))
print(min(answer))
