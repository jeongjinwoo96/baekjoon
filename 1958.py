from itertools import combinations
string = []
for i in range(3):
    string.append(input())
string = sorted(string,key=len)
for i in range(len(string[0]),0,-1):
    for j in list(combinations(string[0],i)):
        flag = True
        idx1 = 0
        idx2 = 0
        for idx in j:
            if idx in string[1] and idx in string[2]:
                if string[1].index(idx) >= idx1 and string[2].index(idx)>=idx2:
                    idx1 = string[1].index(idx)
                    idx2 = string[2].index(idx)
                else:
                    flag = False
                    break
                    
            else:
                flag = False
                break
                
        if flag:
            print(i)
            break
    
    if flag:
        break
