def func(string):
    if not string:
        return True
    if string[:2]=='01':
        return func(string[2:])

    if string[:3]=='100':
        for i in range(3,len(string)):
            if string[i]=='0' and string[i-1]=='1':
                break
        else:
            return int(string[-1]) #100 뒤에 000...11로끝나거나  000만있는 경우
                            #111로 끝났으면 암호 맞음, 0으로 끝났으면 암호아님
        return func(string[i:]) or (int(string[i-2]) and func(string[i-1:]))


N=int(input())
for i in range(N):
    if func(input()):
        print("YES")
    else:
        print("NO")
