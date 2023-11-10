N = int(input())

dic = {}
for i in map(int,input().split()):
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
M = int(input())
for i in map(int,input().split()):
    if i not in dic:
        print(0)
    else:
        print(dic[i])