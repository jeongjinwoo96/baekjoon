n = int(input())
word = []

for i in range(n):
    word.append(input())

answer = n
word = sorted(word, key=lambda x: (x[0], len(x)))

for i in range(n):
    for j in range(i+1,n):
        if word[i] == word[j][0:len(word[i])] :
            answer -= 1
            break
print(answer)
