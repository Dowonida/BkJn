S=input()

L=[]
for i in S:
    L.append(i)
    if L[-4:]==["P","P","A","P"]:
        L.pop()
        L.pop()
        L.pop()
if L==["P"]:
    print("PPAP")
else:
    print("NP")
