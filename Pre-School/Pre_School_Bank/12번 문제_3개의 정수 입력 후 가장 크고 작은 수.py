def num(z,x,y):
    if z>0 and x>0 and y>0 :
        print(max(z,x,y),min(z,x,y))

num(234,3,50)

# ---------------------

# 가장 큰수
a,b,c=input('3개 정수 입력').split(',')
a=int(a)
b=int(b)
c=int(c)
l=(a if a>b else b) if((a if a<b else b)<c) else c
print(l)

# ------------------


# -----------------

a, b, c = map(int, input().split())

print('최소값', min(a, b, c))
print('최대값', max(a, b, c))