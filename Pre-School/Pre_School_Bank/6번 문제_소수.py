# https://curt-park.github.io/2018-09-17/algorithm-primality-test/
# https://hei-jayden.tistory.com/25
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=javaking75&logNo=220787467355

a=int(input('숫자 입력'))
for i in range(2, a+1):
    is_prime = True
    for j in range(2, i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")


# i 값이 2부터 1씩 증가하며 100이 될떄까지 반복
# j 값이 1부터 1씩 증가하며 i-1이 될때까지 반복하고 i를 j로 나눈 나머지가 0이면
# (소수) is_prime에 False를 저장하고 반복문 종료 (break)
# is_prime 값이 False가 아니면 소수이므로 출력


print('\n')

# 소수인지 아닌지
def is_prime_num(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(is_prime_num(3))



for i in range(1,101):
    for j in range(2, i+1):
        if (j == i):
            print(i, end=' ')
        elif (i % j == 0):
            break

# ----------------------

# https://www.youtube.com/watch?v=bBG8TICXVfY

# 소수인지 아닌지
n=int(input('n:'))

check=0
for i in range(1,n+1):
    if n%i == 0:
        check+= 1

if check == 2:
    print(i, True, '소수입니다')

else:
    print(i, False, '소수가 아닙니다.')


# 더 간단하게
n=int(input('n:'))

check=True
for i in range(2,n):
    if n%i == 0:
        check = False

print(check)

# 범위 내의 소수 구하기
# n 값을 입력 받아 1~n 사이 모든 소수값 구하기 (n>0)

a = int(input())
li=[]

for n in range(2,a+1):
    check=True
    for i in range(2,n):
        if n%i == 0:
            check= False

    if check:
        li.append(n)

print(li)
















