a=input()
if a=='0':
    print('W')
elif 'x' not in a:
    if a=='1':
        a=''
    elif a=='-1':
        a='-'
    print(a+'x+W')
    
elif 'x' in a:
    b=a.split('x')
    b[0]=str(int(b[0])//2)
    if b[0]=='1':
        b[0]=''
    elif b[0]=='-1':
        b[0]='-'
    if b[1]=='+1':
        b[1]='+'
    elif b[1]=='-1':
        b[1]='-'
    if b[1]:
        print(b[0]+'xx'+b[1]+'x+W')
    else:
        print(b[0]+'xx'+b[1]+'+W')