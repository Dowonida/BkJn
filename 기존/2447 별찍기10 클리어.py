a='''  *  
 * * 
* * *'''
b='''  
 
'''
def mustpl(a,b):
    A=a.split('\n')
    B=b.split('\n')
    c=''
    for i in range(len(A)):
        c+=B[i]+A[i]+B[i]+'\n'
    for i in range(len(A)):
        c+=A[i]+B[i]+B[i]+A[i]+'\n'
    for i in range(len(A)):
        c+=A[i]+A[i]+A[i]+'\n'
    return c[:-1]


print(a)
