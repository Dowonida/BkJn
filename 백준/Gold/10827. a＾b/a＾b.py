a,b = input().split()
b=int(b)

idx=a.index('.')
cnt=len(a[idx+1:])


a=int(a[:idx]+a[idx+1:])
#자리수는 cnt*b
a**=b

a=format(a,f'0{cnt*b}d')

a=a[:len(a)-cnt*b]+'.'+a[len(a)-cnt*b:]
if a[0]=='.':
    a='0'+a
elif a[-1]=='.':
    a=a[:-1]
print(a)
