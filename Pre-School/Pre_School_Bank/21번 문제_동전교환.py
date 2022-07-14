n=int(input())
a=list(map(int,input().split()))
m=int(input())
dy=[50]*(m+1)
dy[0]=0
for i in range(n) :
    for j in range(a[i],m+1) :
        dy[j]=min(dy[j], dy[j-a[i]]+1)
print(dy[m])

# ------------------

n=int(input())
a=list(map(int,input().split()))
m=int(input())
dy=[50]*(m+1)
dy[0]=0
for i in range(n) :
    for j in range(a[i],m+1) :
        dy[j]=min(dy[j], dy[j-a[i]]+1)
print('거스름동전의개수:',dy[m])
print('설명:',str(a[i])*dy[m],'동전',dy[m],'개로 거슬러 줄 수 있다.')