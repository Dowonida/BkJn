N=int(input())
Map=[[0]*(N+2)]
for i in range(N):
    Map.append([0]+list(map(int,input().split()))+[0])

cnt=N*N+1
for i in range(2**N):

    rst=[[0]*(N+2),[0]]
    for j in range(N):
        rst[1].append(i%2)
        i//=2
    cnt2=sum(rst[1])
    rst[1].append(0)
    for j in range(1,N):
        nextline=[0]
        for k in range(1,N+1):
            nextline.append((rst[j][k]+rst[j][k-1]+rst[j][k+1]+rst[j-1][k]+Map[j][k])%2)
            cnt2+=nextline[-1]
        nextline.append(0)
        rst.append(nextline)
    check=[0]+[(rst[-1][i]+rst[-1][i-1]+rst[-1][i+1]+rst[-2][i]+Map[-1][i])%2 for i in range(1,N+1)]+[0]
    if sum(check)==0 and cnt2<cnt:
        cnt=cnt2
if cnt==N*N+1:
    print(-1)
else:
    print(cnt)

#전구끄기와 동일하다. 맨 윗줄의 스위치on off여부를 전부 선택해주면
#다음 줄의 스위치on off여부는 자동으로 정해진다.
#왜냐하면 1번줄 스위치의 on off가 다 정해진 상태에서 1번줄의 전구 on off를 맞춰주려면
#상,좌우로 인접한 스위치는 이미 다 누른 상태이므로 아래에 인접한 스위치가 결과에 맞춰서 눌러야하기 때문
#그럼 1번줄의 스위치의 경우의 수가 2**N이므로 모든 경우의 수에 따라서 일단 처리를 하고
#마지막 스위치의 on off까지 다 구한 다음에 전구의 상태가 일치하는지 확인하면 된다.
#이 때, 1~N-1번 줄의 스위치는 알아서 맞춰지게 셋팅을 했으므로 마지막 줄만 확인하면 된다.
#확인결과가 맞게 나왔을 경우 스위치를 누른 횟수가 가장 적은 것으로 계속 갱신한다.